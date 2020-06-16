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

list_of_vms = []

# If resource group is specified, find VMs under that resource group.
rg = ''
try:
  rg=relay.get(D.resourceGroup)
except:
  print('No resource group found. Looking up all Virtual Machines under subscription id.')

if (rg):
 print('Looking up all Virtual Machines under resource group {0}:'.format(rg))
 virtual_machines = compute_client.virtual_machines.list(rg)

# Get all VMs under a Subscription ID
else: 
  virtual_machines = compute_client.virtual_machines.list_all()

# Append VM resource IDs to list
print ("\n{:<30} {:<30} {:<30} {:<30}".format('NAME', 'LOCATION', 'VM SIZE', 'TAGS')) 
for virtual_machine in virtual_machines:
  print("{:<30} {:<30} {:<30} {:<30}".format(virtual_machine.name, virtual_machine.location, virtual_machine.hardware_profile.vm_size, str(virtual_machine.tags)))
  list_of_vms.append(virtual_machine.as_dict())

# Setting output variable `virtualMachines` to list of Azure Virtual Machines
print('Setting output `virtualMachines` to list of {0} found virtual machines'.format(len(list_of_vms)))
relay.outputs.set('virtualMachines', list_of_vms)