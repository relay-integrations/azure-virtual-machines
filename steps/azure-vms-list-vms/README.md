# azure-vms-list-vms

This [Azure](https://azure.microsoft.com/en-us/services/virtual-machines/) step container lists the virtual machines in an Azure subscription or resource group and sets an output, `virtualMachines`, to an array of virtual machine objects.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `azure` || mapping | A mapping of Azure account configuration. | None | True |
|| `connection` | Azure Connection | Connection for the Azure account. Use the Connection sidebar to configure the Azure Connection | None | True |
| `resourceGroup` || string | Resource group to look up virtual machines under | None | False | 

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `virtualMachines` | array of Azure Virtual machines | List of Azure virtual machines and metadata. |

## Example

```yaml
steps:
# ...
- name: azure-vms-list-vms
  image: projectnebula/azure-vms-list-vms
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    resourceGroup: 'my_resource_group' 
```

## Example output `virtualMachines`
```
[
  {
    "additionalCapabilities": null,
    "availabilitySet": null,
    "diagnosticsProfile": {
      "bootDiagnostics": {
        "enabled": true,
        "storageUri": "https://linuxvm1cc4de86a.blob.core.windows.net/"
      }
    },
    "hardwareProfile": {
      "vmSize": "Standard_D3_v2"
    },
    "id": "/subscriptions/c82736ee-c108-452b-8178-f548c95d18fe/resourceGroups/TESTER/providers/Microsoft.Compute/virtualMachines/linux-vm1",
    "identity": null,
    "instanceView": null,
    "licenseType": null,
    "location": "ukwest",
    "name": "linux-vm1",
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/c82736ee-c108-452b-8178-f548c95d18fe/resourceGroups/tester/providers/Microsoft.Network/networkInterfaces/linux-vm1-nic",
          "primary": null,
          "resourceGroup": "tester"
        }
      ]
    },
    "osProfile": {
      "adminPassword": null,
      "adminUsername": "testing",
      "allowExtensionOperations": null,
      "computerName": "linux-vm1",
      "customData": null,
      "linuxConfiguration": {
        "disablePasswordAuthentication": false,
        "provisionVmAgent": null,
        "ssh": null
      },
      "secrets": [],
      "windowsConfiguration": null
    },
    "provisioningState": "Succeeded",
    "resourceGroup": "TESTER",
    "resources": [
      {
        "autoUpgradeMinorVersion": null,
        "forceUpdateTag": null,
        "id": "/subscriptions/c82736ee-c108-452b-8178-f548c95d18fe/resourceGroups/TESTER/providers/Microsoft.Compute/virtualMachines/linux-vm1/extensions/CustomScriptExtension",
        "instanceView": null,
        "location": null,
        "name": null,
        "protectedSettings": null,
        "provisioningState": null,
        "publisher": null,
        "resourceGroup": "TESTER",
        "settings": null,
        "tags": null,
        "type": null,
        "typeHandlerVersion": null,
        "virtualMachineExtensionType": null
      }
    ],
    "storageProfile": {
      "dataDisks": [],
      "imageReference": {
        "id": null,
        "offer": "Puppet-Enterprise",
        "publisher": "Puppet",
        "sku": "2017-2",
        "version": "latest"
      },
      "osDisk": {
        "caching": "ReadWrite",
        "createOption": "FromImage",
        "diffDiskSettings": null,
        "diskSizeGb": 30,
        "encryptionSettings": null,
        "image": null,
        "managedDisk": {
          "id": "/subscriptions/c82736ee-c108-452b-8178-f548c95d18fe/resourceGroups/tester/providers/Microsoft.Compute/disks/linux-vm1_OsDisk_1_19610e1d78324f368d234bff95458f0b",
          "resourceGroup": "tester",
          "storageAccountType": "Standard_LRS"
        },
        "name": "linux-vm1_OsDisk_1_19610e1d78324f368d234bff95458f0b",
        "osType": "Linux",
        "vhd": null,
        "writeAcceleratorEnabled": null
      }
    },
    "tags": null,
    "type": "Microsoft.Compute/virtualMachines",
    "vmId": "9c15c645-bf0a-452b-9ae4-62a03b15af8a",
    "zones": null
  }
]
```