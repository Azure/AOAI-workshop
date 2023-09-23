# "Hey cinema!" Demo  

## Azure Text to Speech -> OpenAI -> Speech to Text Python Examples

This repository contains Python code examples that demonstrate how to use the Azure Cognitive Services Speech SDK for both text-to-speech (TTS) and speech-to-text (STT) tasks, and in the middle query OpenAI's API

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

2. Clone the repository:

    ```shell
    git clone https://github.com/vladfeigin/openaiworkshop.git
    cd openaiworkshop
    ```  
---

## Usage

1. Replace the placeholders in the Python code files with your Azure Speech Service API keys and service region.

2. **Text to Speech**  
    Taken from the documentation's TTS "Getting started" guide:
    [Click Here](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=macos%2Cterminal&pivots=programming-language-python)  
    To convert text to speech, run:

    ```shell
    python 01_speech_to_text.py
    ```

    This script takes a text input and converts it into speech, saving the output as an audio file.

3. **Speech to Text**  
    Taken from the documentation's STT "Getting started" guide:
    [Click Here](https://learn.microsoft.com/en-us/azure/cognitive-services/Speech-Service/get-started-text-to-speech?tabs=macos%2Cterminal&pivots=programming-language-python)  
    To transcribe speech into text, run:

    ```shell
    python 02_text_to_speech.py
    ```

    This script takes an audio file as input and transcribes the speech into text.

4. **Embedding CSV Movies**  

    This is a notebook: 
    ```03_embedding_csv_demo.ipynb```  

    It takes 1000 movies data into OpenAI's API and you can ask questions to query the data

5. **Hey Cinema**  

    This one pulls everything together:

    ```shell
    python 04_hey_cinema_full.py
    ```

    It uses all the previous demos' code here, so you can speak your question, which will go to the Azure-OpenAI's API and they speak back your answers (up to 3 answers)

---
## Data origin:
- [IMDB data](https://raw.githubusercontent.com/laxmimerit/All-CSV-ML-Data-Files-Download/master/IMDB-Movie-Data.csv)

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


