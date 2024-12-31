"""This module has functionalities for NLP sentiment analysis on the cloud
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """This function querys IBM Watson AI for NLP sentiment analysis
    Args:
        text_to_analyse (str): The raw text to analyse for sentiment

    Returns:
        (dict): Returns a dict of label (sentiment) and score
    """

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1' + \
    '/watson.runtime.nlp.v1/NlpService/SentimentPredict'  
    myobj = {"raw_document": { "text": text_to_analyse }}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=(3, 10))
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        return {
            "label" : formatted_response['documentSentiment']['label'],
            "score":  formatted_response['documentSentiment']['score']
        }

    return {
        "label" : None,
        "score":  None
    }
