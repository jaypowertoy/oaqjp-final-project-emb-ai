import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyse):
    """Define a function that analyzes sentiment of the provided text."""
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Create a dictionary with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Set the headers required for the API request
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Return the response text from the API
    return response.text
