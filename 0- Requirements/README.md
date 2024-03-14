For this workshop you MUST have the following:

# Requirements
- Visual Studio Code
- Python (tested with 3.10, 3.12)
- Pyhton virtual environment tool (venv)
- An Azure account 
- Azure subscription onboarded into Azure OpenAI
- Necessary permissions to deploy resources in the subscription

# Preparation

## Git repository
- Clone this repository to your local machine and open a terminal in the cloned directory.

## Visual Studio Code
- Windows
    - Install [Visual Studio Code](https://code.visualstudio.com/)
- Linux
    - Install [Visual Studio Code](https://code.visualstudio.com/)
- Mac
    - Install [Visual Studio Code](https://code.visualstudio.com/)

## Python
- Windows
    - Install [Python 3.12.2](https://www.python.org/downloads/release/python-3122/)
- Linux
    - It is usually pre-installed. Check version with `python3 --version`.
- Mac
    - `brew install python3`

### Python Virtual Environment Setup
-  To install virtualenv via pip run:
    - Windows / Mac / Linux:

         `pip3 install virtualenv`

- Creation of virtualenv (in the cloned Azure/AOAI-workshop directory):
    - Windows:

        `python -m virtualenv venv`
    - Mac / Linux:

        `virtualenv -p python3 venv`

- Activate the virtualenv:
    - Windows:

        `.\venv\Scripts\activate.ps1`
    - Mac / Linux

        `source ./venv/bin/activate`

### Install required libraries in your virtual environment
- Run the following command in the terminal:
    - Windows / Mac / Linux:

        `pip3 install -r requirements.txt`

## Create the necessary Azure resources
- Insert your subscription ID in the file [createAll.ps1](./scripts/createAll.ps1) and save it. 
    ```
    $SubscriptionId = "<your subscription here>"
    ```
- Modify the password of the admin user of the SQL database the file [deployAll.bicep](./scripts/deployAll.bicep) and save it. 
    ```
    param adminPassword string = 'ChangeYourAdminPassword1'
    ```
- This powershell script will create:
    - A resource group with name starting with 'openai-workshop'
    - An Azure SQL server with an AdventureWorks sample database
    - An AI Search service
    - An AI Speech service
    - An AI Vision service
    - An Azure OpenAI service with the following models:
        - GPT-3.5
        - GPT-4
        - GPT-4 Vision
        - DALL-E
        - Text Embedding Ada


- Go to the azure portal and login with a user that has permissions to create resource groups and resources in your subscription.
- Open the cloud shell in the azure portal as follows:
![Cloud shell](./images/step2.png)

- Upload the files located in the `scripts` folder `createAll.ps1` and `deployAll.bicep`, ONE BY ONE by using the upload file button in the cloud shell:
![Upload](./images/step3.png)

- Run `./createAll.ps1` in the cloud shell to create the resources:
![Upload](./images/step4.png)

    *NOTE: This takes time so be patient.*

- You should get a resource group with the following resources:
![Upload](./images/step5.png)

# IMPORTANT!
## Setup environment variables
- Duplicate the `.env.template` file and rename the new file to `.env`.
- Open your new `.env` file and modify all the endpoints and api keys for all deployments as follows:
```
# Open AI details
OPENAI_GPT35_DEPLOYMENT_NAME="gpt-35-turbo-16k"
OPENAI_GPT4_DEPLOYMENT_NAME="gpt-4"
OPENAI_GPT4V_DEPLOYMENT_NAME="gpt-v"
OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME="text-embedding-ada-002"
OPENAI_DALLE_DEPLOYMENT_NAME="dall-e-3"

OPENAI_DEPLOYMENT_ENDPOINT="<your azure openai deployment url>" 
OPENAI_API_KEY="<the key to the azure open ai service>"

# SQL Server details
SQL_USER="SqlAdmin"
SQL_DBNAME="aworks"

SQL_SERVER="<your sql server url>"
SQL_PWD="<the password you defined in the bicep file>"


# AI Speech details
SPEECH_REGION="westeurope"

SPEECH_KEY="<the key for the ai speech service>"

# AI Vision details
VISION_REGION="swedencentral"

AZURE_COMPUTER_VISION_ENDPOINT="<azure ai vision deployment url>"
AZURE_COMPUTER_VISION_KEY="<the key to the ai vision service>"

# AI Search details
AZURE_SEARCH_SERVICE_ENDPOINT="<your azure ai search deployment url>"
AZURE_SEARCH_ADMIN_KEY="<the management key of the ai search>"
```