# azure-virtual-machines-step-vm-deallocate

This [Azure](https://azure.microsoft.com/en-us/services/virtual-machines/) step container deallocates a set of Azure virtual machines in an Azure subscription given a set of resource IDs. Deallocated VMs do not incurring billing charges.

## Notes
To get the Azure VM resource IDs, try the following command using the Azure CLI: 
 ```
 $ az vm list | jq ".[].id"

"/subscriptions/c8236dee-c104-452b-8128-f448c65d18fe/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/my-vm-1"
"/subscriptions/c8236dee-c104-452b-8128-f448c65d18fe/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/my-vm-2"
```

For more information on Resource IDs, check out the [documentation](https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid). 
