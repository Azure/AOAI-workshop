#%%

# imports
import os
import azure.cognitiveservices.speech as speechsdk

from dotenv import load_dotenv

# load environment variables
load_dotenv()

SPEECH_KEY                        = os.getenv("SPEECH_KEY")
SPEECH_REGION                     = os.getenv("SPEECH_REGION")

default_text                      = """ 
    Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness, 
    for he is truly his brother's keeper and the finder of lost children. 
    And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy My brothers.
"""

default_text                      = """ 
    And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy My brothers.
"""

def text_to_speech(text, voice="en-US-JennyNeural"):
    # Create a speech synthesizer using the default speaker as audio output.
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = voice
    
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")


# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want me to read out loud ==>")
text = input()
if len(text) == 0:
    text = default_text
# print(len(text))

# the full list of supported voices can be found here:
# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#text-to-speech

israeli_voice  = 'he-IL-HilaNeural'
american_voice = 'en-US-RogerNeural'

text_to_speech(text, voice=american_voice)

# he-IL-HilaNeural

# %%
