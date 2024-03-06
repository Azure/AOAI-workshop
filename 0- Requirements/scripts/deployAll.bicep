// General params
param location string = resourceGroup().location

// SQL Server params
param serverName string = 'sqlserver-${uniqueString(resourceGroup().id)}'
param databaseName string = 'aworks'
param adminLogin string = 'SqlAdmin'
@secure()
param adminPassword string = 'ChangeYourAdminPassword1'

// Speech Service params
param SpeechServiceName string = 'aispeech-${uniqueString(resourceGroup().id)}'
param speech_location string = 'westeurope'

// OpenAI params
param OpenAIServiceName string = 'openai-${uniqueString(resourceGroup().id)}'
param openai_deployments array = [
  {
    name: 'text-embedding-ada-002'
	  model_name: 'text-embedding-ada-002'
    version: '2'
    raiPolicyName: 'Microsoft.Default'
    sku_capacity: 20
    sku_name: 'Standard'
  }
  {
    name: 'gpt-35-turbo-16k'
	  model_name: 'gpt-35-turbo-16k'
    version: '0613'
    raiPolicyName: 'Microsoft.Default'
    sku_capacity: 20
    sku_name: 'Standard'
  }
  {
    name: 'gpt-4'
	  model_name: 'gpt-4'
    version: '1106-Preview'
    raiPolicyName: 'Microsoft.Default'
    sku_capacity: 20
    sku_name: 'Standard'
  }
  {
    name: 'gpt-4'
	  model_name: 'gpt-v'
    version: 'vision-preview'
    raiPolicyName: 'Microsoft.Default'
    sku_capacity: 20
    sku_name: 'Standard'
  }
  {
    name: 'dall-e-3'
	  model_name: 'dall-e-3'
    version: '3.0'
    raiPolicyName: 'Microsoft.Default'
    sku_capacity: 1
    sku_name: 'Standard'
  }
]

// AI Search params
param aisearch_name string = 'aisearch-${uniqueString(resourceGroup().id)}'

resource sqlServer 'Microsoft.Sql/servers@2021-02-01-preview' = {
  name: serverName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    administratorLogin: adminLogin
    administratorLoginPassword: adminPassword
  }
}

resource sqlServerFirewallRules 'Microsoft.Sql/servers/firewallRules@2020-11-01-preview' = {
  parent: sqlServer
  name: 'Allow Azure Services'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '255.255.255.255'
  }
}

resource sqlDatabase 'Microsoft.Sql/servers/databases@2021-02-01-preview' = {
  name: databaseName
  parent: sqlServer
  location: location
  properties: {
    collation: 'SQL_Latin1_General_CP1_CI_AS'
    sampleName: 'AdventureWorksLT'
  }
}

resource cognitiveService 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: SpeechServiceName
  location: speech_location
  sku: {
    name: 'S0'
  }
  kind: 'SpeechServices'
  properties: {
    apiProperties: {
      statisticsEnabled: false
    }
  }
}

resource openai 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: OpenAIServiceName
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'OpenAI'
  properties: {
    apiProperties: {
      statisticsEnabled: false
    }
  }
}

@batchSize(1)
resource model 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = [for deployment in openai_deployments: {
  name: deployment.model_name
  parent: openai
  sku: {
	name: deployment.sku_name
	capacity: deployment.sku_capacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: deployment.name
      version: deployment.version
    }
    raiPolicyName: deployment.raiPolicyName
  }
}]

resource search 'Microsoft.Search/searchServices@2020-08-01' = {
  name: aisearch_name
  location: location
  sku: {
    name: 'basic'
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
  }
}