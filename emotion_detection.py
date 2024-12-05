'''This is a module that utilizes the requests
   and the built in json library to analyze text
   and return a value representative of the emotions
   conveyed.
'''
import requests
import json

def emotion_detector(text_to_analyze):
    '''This is a function that will accept a string as an input
       and implement the requests library to return a string representing the
       emotional content of the text
    '''
    # These are the values needed for the HTTP API call to watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body_object = { "raw_document": { "text": text_to_analyze } }
    # Utilizing the requests library to analyze the text from the args
    response = requests.post(url, json=body_object, headers=headers, timeout=1.00)

    return response.text