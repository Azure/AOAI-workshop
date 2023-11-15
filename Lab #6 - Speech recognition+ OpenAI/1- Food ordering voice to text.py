# Food orders – speech to text to JSON – get a food order, use Azure AI Speech Cognitive service to transform 
# speech to text and then using Azure OpenAI GPT3.5 to extract a JSON object that represents the order and can be used to search in a Database
# In this case we are extracting restaurant order entities.
# try saying:  I would like to order a large burger which French fries and a large coke.

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import pandas as pd
import openai
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")

openai.api_type = "azure"
openai.api_base = OPENAI_DEPLOYMENT_ENDPOINT
openai.api_version = "2023-07-01-preview"
openai.api_key = OPENAI_API_KEY

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

def voice_to_text():
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Can I have your order please?")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Text: {}".format(speech_recognition_result.text))
    return speech_recognition_result.text

def call_openAI(text):

    message_text = [
    {"role":"system","content":"You are an assistant designed to extract entities from a food order transcript. Users will enter in a string of text and you will respond with entities you\'ve extracted from the text as a JSON object. Here\'s an example of your output format:[  {    main: {      type: \"vegan burger\",      size: \"large\",      cooking_degree: \"medium\",      toppings: [        {          type: \"lettuce\",          quantity: 1,          size: \"small\"        },        {          type: \"tomato\",          quantity: 1,          size: \"\"        },        {          type: \"onion\",          quantity: 2,          size: \"\"        }      ]    },drinks: {  type: \"pepsi cola\",  size: \"large\",  additionals: [{  type: \"ice\",  quantity: 1,  size: \"small\"},{  type: \"lemon\",  quantity: 1,  size: \"\"}  ]}  }]"},
    {"role":"user","content":text}]

    completion = openai.ChatCompletion.create(
    engine=OPENAI_DEPLOYMENT_NAME,
    messages = message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )
    return completion.choices[0].message.content


#I would like to order two hamburgers with French fries, tomato, lettuce and mayonnaise and two large cokes and two ice creams
if __name__ == "__main__":
    text = voice_to_text()
    response = call_openAI(text)
    print(response)
