import requests
import json


def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Custom header specifying the model ID for the emotion detection service
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Sending a POST request to the emotion detection API
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)

        # Check for status code 400 (blank/invalid input)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

    # Parsing the JSON response from the API
    try:
        formatted_response = json.loads(response.text)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Response text: {response.text}")
        return None

    # Extracting emotion predictions from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extract individual emotion scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Returning a dictionary containing emotion analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
