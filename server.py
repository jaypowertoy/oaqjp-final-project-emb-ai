"""Flask server for Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Endpoint to detect emotions in the provided text.

    Query parameter:
        textToAnalyze: The text statement to analyze

    Returns:
        Formatted string with emotion scores and dominant emotion
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Handle error case
    if result is None:
        return "Error processing the request. Please try again."

    # Format the response as specified
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
