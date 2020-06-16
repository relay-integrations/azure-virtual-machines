# azure-virtual-machines-step-vm-delete

This [Azure](https://azure.microsoft.com/en-us/services/virtual-machines/) step container deletes a set of
Azure virtual machines in an Azure subscription given a set of resource IDs. 

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `azure` || mapping | A mapping of Azure account configuration. | None | True |
|| `connection` | Azure Connection | Connection for the Azure account. Use the Connection sidebar to configure the Azure Connection | None | True |
| `resourceIDs` ||  An array of Azure Virtual Machine resource IDs | The list of resource IDs of the Azure Virtual Machines to be deleted | None | True |
| `waitForDeletion` ||  boolean | Determines whether to wait for Virtual Machines to be deleted before continuing | False | False | 

## Outputs
None

## Example  

```yaml
steps:
# ...
- name: azure-vms-delete-vms
  image: relaysh/azure-virtual-machines-step-vm-delete
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    waitForDeletion: true 
    resourceIDs:
    - /subscriptions/c8236dee-c104-452b-8128-f448c65d18fe/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/my-vm-1
    - /subscriptions/c8236dee-c104-452b-8128-f448c65d18fe/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/my-vm-2
```

## Notes
To get the Azure VM resource IDs, try the following command using the Azure CLI: 
 ```
 $ az vm list | jq ".[].id"

"/subscriptions/c8236dee-c104-452b-8128-f448c65d18fe/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/my-vm-1"
"/subscriptions/c8236dee-c104-452b-8128-f448c65d18fe/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/my-vm-2"
```

For more information on Resource IDs, check out the [documentation]("https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid"). 

