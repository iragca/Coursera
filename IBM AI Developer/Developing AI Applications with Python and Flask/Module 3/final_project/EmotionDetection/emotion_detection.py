"""Emotion Detection Module

This module provides functionalities for detecting emotions in a given text using 
IBM Watson's NLP library. The primary function, `emotion_detector`, sends a text input 
to IBM Watson's Emotion Detection API and returns the predicted emotion and its associated score.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """Detect emotions in text using IBM Watson NLP.

    This function queries IBM Watson's NLP Emotion Detection API 
    to analyze the provided text and identify the dominant emotion. 
    It returns the predicted emotion label and its confidence score.

    Args:
        text_to_analyze (str): The input text to analyze for emotions.

    Returns:
        dict: A dictionary containing:
            - "emotion" (str): The label of the predicted emotion (e.g., "joy", "sadness").
            - "score" (float): The confidence score for the predicted emotion (between 0 and 1).
            If the API call fails, both values will be set to `None`.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the API request 
            (e.g., network errors or timeout).
    """

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1'
        '/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    # Prepare the payload and headers for the API request
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send the request to the API
    response = requests.post(url, json=myobj, headers=header, timeout=(3, 10))
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # Extract emotion predictions and determine the best prediction
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    best_prediction_value = 0
    best_prediction_emotion = None

    for key, value in emotions.items():
        if float(value) > best_prediction_value:
            best_prediction_value = value
            best_prediction_emotion = key

    # Check if the response was successful and return the results
    if response.status_code == 200:
        emotions['dominant_emotion'] = best_prediction_emotion
        return emotions
