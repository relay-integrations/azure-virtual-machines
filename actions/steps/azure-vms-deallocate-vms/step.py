#!/usr/bin/env python

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from nebula_sdk import Interface, Dynamic as D


relay = Interface()

credentials = ServicePrincipalCredentials(
    client_id=relay.get(D.azure.connection.clientID),
    secret=relay.get(D.azure.connection.secret),
    tenant=relay.get(D.azure.connection.tenantID)
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

print('Deallocating {} Azure Virtual machine(s)'.format(len(resource_ids)))

# Deallocates each VM in list_of_vms
vm_handle_list = []
for resource_id in resource_ids:
  resource_group_name = resource_id.split('/')[4] # Resource group name
  vm_name = resource_id.split('/')[8] # VM name
  print('Deallocating Azure Virtual Machine {0} in Resource Group {1}'.format(vm_name, resource_group_name))  
  async_vm_operation = compute_client.virtual_machines.deallocate(resource_group_name, vm_name)
  vm_handle_list.append(async_vm_operation)


# If wait is set, wait for VMs to terminate before exiting.
if wait: 
  for async_vm_operation in vm_handle_list:
    print('Waiting for Azure Virtual Machine to be deallocated.')
    async_vm_operation.wait()

print('All specified Azure Virtual Machines are deallocated.')

