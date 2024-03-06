$SubscriptionId = ''
$GUID = New-Guid
$resourceGroupName = "openai-workshop-$GUID"
$location = "swedencentral"

# Set subscription 
Set-AzContext -SubscriptionId $subscriptionId 
# Create a resource group
New-AzResourceGroup -Name $resourceGroupName -Location $location

New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile deployAll.bicep -WarningAction:SilentlyContinue