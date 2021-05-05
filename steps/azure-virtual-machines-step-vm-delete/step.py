#!/usr/bin/env python

from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from relay_sdk import Interface, Dynamic as D
import logging

logging.basicConfig(level=logging.WARNING)

relay = Interface()

credentials = ClientSecretCredential(
    client_id=relay.get(D.azure.connection.clientID),
    client_secret=relay.get(D.azure.connection.secret),
    tenant_id=relay.get(D.azure.connection.tenantID)
)
subscription_id=relay.get(D.azure.connection.subscriptionID)
compute_client = ComputeManagementClient(credentials, subscription_id)


# Getting resource ids & options
resource_ids = None
wait = False 

try:
  resource_ids = relay.get(D.resourceIDs)
except:
  print('No Resource IDs found. Exiting.')
  exit

try:
  wait = relay.get(D.waitForDeletion)
except:
  pass

print('Deleting {} Azure Virtual machine(s)'.format(len(resource_ids)))

# Deletes each VM in resource_id list 
vm_handle_list = []
for resource_id in resource_ids:
  resource_group_name = resource_id.split('/')[4] # Resource group name
  vm_name = resource_id.split('/')[8] # VM name
  print('Deleting Azure Virtual Machine {0} in Resource Group {1}'.format(vm_name, resource_group_name))  
  async_vm_operation = compute_client.virtual_machines.begin_delete(resource_group_name, vm_name)
  vm_handle_list.append(async_vm_operation)


# If wait is set, wait for VMs to terminate before exiting.
if wait: 
  for async_vm_operation in vm_handle_list:
    print('Waiting for Azure Virtual Machine to be deleted.')
    async_vm_operation.wait()

print('All specified Azure Virtual Machines are deleted.')
