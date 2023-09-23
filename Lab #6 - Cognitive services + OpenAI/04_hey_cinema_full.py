#%%
import os
import openai
import pandas                         as pd
import numpy                          as np
import azure.cognitiveservices.speech as speechsdk

from dotenv                  import load_dotenv
from openai.embeddings_utils import cosine_similarity, get_embedding

# load environment variables
load_dotenv()
OPENAI_API_KEY                       = os.getenv("OPENAI_API_KEY") 
OPENAI_DEPLOYMENT_ENDPOINT           = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME               = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME                    = os.getenv("OPENAI_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION            = os.getenv("OPENAI_DEPLOYMENT_VERSION")

OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_ADA_EMBEDDING_MODEL_NAME      = os.getenv("OPENAI_ADA_EMBEDDING_MODEL_NAME")

OPENAI_DAVINCI_DEPLOYMENT_NAME       = os.getenv("OPENAI_DAVINCI_DEPLOYMENT_NAME")
OPENAI_DAVINCI_MODEL_NAME            = os.getenv("OPENAI_DAVINCI_MODEL_NAME")

SPEECH_KEY                           = os.getenv("SPEECH_KEY")
SPEECH_REGION                        = os.getenv("SPEECH_REGION")

# Configure OpenAI API
openai.api_type    = "azure"
openai.api_version = OPENAI_DEPLOYMENT_VERSION
openai.api_base    = OPENAI_DEPLOYMENT_ENDPOINT
openai.api_key     = OPENAI_API_KEY


def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language="en-US"

    audio_config      = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return speech_recognition_result.text

def text_to_speech(text, voice="en-US-JennyNeural"):
    speech_config                             = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config                              = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name = voice
    speech_synthesizer                        = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result                   = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")


def ask_question(question, n=1):
    question_embedding = get_embedding(
        question,
        engine=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME
    )

    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, question_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )

    answer =  ' \n'.join(results.All.tolist()) 
    print("Answer:\n", answer)
    return answer


# Load the data
datafile_path = "./data/imdb_movies_with_embeddings.csv"
df = pd.read_csv(datafile_path)
df["embedding"] = df.embedding.apply(eval).apply(np.array)

american_voice = 'en-US-RogerNeural'

# listen to the question
print("Please tell me which kind of movie are you looking for? ==>")
question_text = recognize_from_microphone()
# ask the question
answer_text   = ask_question(question=question_text, n=3)
# speak the answer
text_to_speech(answer_text, voice=american_voice)

