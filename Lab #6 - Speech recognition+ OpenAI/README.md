## Azure Text to Speech -> OpenAI -> Speech to Text Python Examples

This repository contains Python code examples that demonstrate how to use the Azure Cognitive Services Speech SDK for both text-to-speech (TTS) and speech-to-text (STT) tasks, and  OpenAI's API

## Features

- **Text to Speech**: Convert written text into natural sounding speech.
- **Azure OpenAI**  : Embedding model.
- **Speech to Text**: Transcribe spoken language into written text.

## Prerequisites

- Python 3.7.1 or later
- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/cognitive-services/)
- The Azure Speech service - You'll need to [create a Speech resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices) in the Azure portal to get your API keys.
- AzureOpenAI [Click here](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/quickstart?tabs=command-line&pivots=programming-language-python)  
  
---  

## Setup

1. Install the necessary Python package dependencies:

    ```shell
    pip install -r requirements.txt
    ```  
---

## Usage

1. Replace the placeholders in the Python code files with your Azure Speech Service API keys and service region.

2. **Speech to Text**  
    Taken from the documentation's STT "Getting started" guide:
    [Click Here](https://learn.microsoft.com/en-us/azure/cognitive-services/Speech-Service/get-started-text-to-speech?tabs=macos%2Cterminal&pivots=programming-language-python)  
    To transcribe speech into text, run:

    ```shell
    python '.\1- Food ordering voice to text.py'
    ```

    This script takes an audio file as input and transcribes the speech into text.


## Bonus material:  
- [Speech to text?](https://www.youtube.com/watch?v=qM79_itR0Nc)  
- [Movie Phone hits again](https://www.youtube.com/watch?v=xm4mDO4XGIE)  
  
---
## Documentation

For more details on Azure Cognitive Services Speech SDK, check out  
- **[Azure Documentation](https://docs.microsoft.com/azure/cognitive-services/speech-service/)**  
- **[Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)**   


## License

This project is licensed under the MIT License. 

## Issues  

If you encounter any issues or have any questions, feel free to open an issue in the repository.  

---  


