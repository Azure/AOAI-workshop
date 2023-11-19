For this workshop you MUST have the following:

## Requirements
- VsCode
- Python 3.7
- A virtual environment tool (venv)
- An Azure account 
- An active Azure OpenAI account with 2 deployed models see below

## Preparation

## OpenAI subscription and deployments
* Create an Azure OpenAI account
* Create 'gpt-35-turbo','text-embedding-ada-002' deployments

### VsCode
* Install [Visual Studio Code](https://code.visualstudio.com/)

### Python
* Install [Python 3.7](https://www.python.org/downloads/release/python-31011/)

### Python3 Virtualenv Setup
*  Installation
        To install virtualenv via pip run:
            $ pip3 install virtualenv
* Creation of virtualenv:
    - Windows
    $ python -m virtualenv venv (in the openAI workshop directory)
    - Mac
    $ virtualenv -p python3 <desired-path>

    Activate the virtualenv:
    $ source <desired-path>/bin/activate

    Deactivate the virtualenv:
    $ deactivate

#### Python3 Virtualenv Setup
*  Installation
        To install virtualenv via pip run:
            $ pip3 install virtualenv
* Creation of virtualenv:
    - Windows
    $ python -m virtualenv venv (in the openAI workshop directory)
    - Mac
    $ virtualenv -p python3 <desired-path>

### Install all libraries in your virtual environment
* Activate the environment
    Windows:
        .\venv\Scripts\activate.ps1
    Mac:
    $ source ./venv/bin/activate

* Make sure you have the requirements installed in your Python environment using `pip install -r requirements.txt`.


### Create a sample Azure SQL DB with Adventureworks sample data
* Insert your subscription ID in the file [createAll.ps1](./scripts/createAll.ps1) and save it. 
    ```
    $SubscriptionId = "<your subscription here>"
    ```
* Insert a name for your sql server in the file [deployAll.bicep](./scripts/deployAll.bicep) and save it
    ```
    param serverName string = '<sql server name>'
    ```
* This powershell script will create:
    * A resourcegroup called openai-workshop
    * An Azure SQL server called <your sql server name> with an AdventureWorks DB

* Go to the azure portal and login with a user that has administrator permissions
* Open the cloud shell in the azure portal as follows:
![Cloud shell](./images/step2.png)

* Upload the files in the scripts folder: "createAll.ps1" and "deployAll.bicep" ONE BY ONE by using the upload file button in the cloud shell
![Upload](./images/step3.png)

* Run ./createAll.ps1
![Upload](./images/step4.png)
NOTE: This takes time so be patient
You should get an Azure SQL server with a DB called aworks
![Upload](./images/step5.png)

# IMPORTANT!
### Setup environment variables
* Rename the '.env.template' file to '.env' and modify all the endpoints and api keys for all deployments as follows:
```
OPENAI_DEPLOYMENT_ENDPOINT ="<your openai endpoint>" 
OPENAI_API_KEY = "<your openai api key>"
OPENAI_DEPLOYMENT_NAME = "<your gpt35 deployment name>"
OPENAI_DEPLOYMENT_VERSION = "<gpt35 api version>"
OPENAI_MODEL_NAME="<gpt35 model name>"

OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = "<your text embedding ada deployment name>"
OPENAI_ADA_EMBEDDING_MODEL_NAME = "<your text embedding ada model name>"

OPENAI_DAVINCI_DEPLOYMENT_NAME = "<your text embedding ada deployment name>"
OPENAI_DAVINCI_MODEL_NAME = "<your da vinci model name>"

SQL_SERVER="<sql server name>.database.windows.net"
SQL_USER="SqlAdmin"
SQL_PWD="ChangeYourAdminPassword1"
SQL_DBNAME="aworks"

# cognitive services speech
SPEECH_KEY       = "<your speech key>"
SPEECH_REGION    = "<your speech region>"

AZURE_COMPUTER_VISION_ENDPOINT="<your computer vision endpoint>"
AZURE_COMPUTER_VISION_KEY="<your computer vision key>"
AZURE_SEARCH_SERVICE_ENDPOINT="<your search service endpoint>"
AZURE_SEARCH_INDEX_NAME="<your search index name>"
AZURE_SEARCH_ADMIN_KEY="<your search admin key>"

AAD_TENANT_ID = "<your aad tenant id>"
KUSTO_CLUSTER =  "https://<your azure data explorer name>.westeurope.kusto.windows.net"
KUSTO_DATABASE = "<your kusto database name>"
KUSTO_TABLE = "wikipedia"
KUSTO_MANAGED_IDENTITY_APP_ID = "<your aad app registration id>"
KUSTO_MANAGED_IDENTITY_SECRET = "<your kusto managed identity secret>"

OPENAI_DALLE_ENDPOINT = "<your openai dalle endpoint>"
OPENAI_DALLE_API_KEY = "<your openai dalle api key>"
OPENAI_DALLE_DEPLOYMENT_NAME = "<your openai dalle model name>"
```