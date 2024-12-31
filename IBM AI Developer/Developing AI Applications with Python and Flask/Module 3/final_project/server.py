"""Emotion Detector Flask Application

This module defines a simple Flask web application that allows users to input a text string
and receive an analysis of the emotions expressed within the text. The system detects various 
emotions, such as anger, joy, fear, sadness, and disgust, and identifies the dominant emotion. 
The application provides the emotion analysis via a web interface.

Routes:
    - /: Displays the main page of the application where users can input text.
    - /emotionDetector: Handles the emotion detection for 
                        the given text and returns the emotion scores.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_index_page():
    """Renders the main application page where users can input text for emotion detection.
    
    Returns:
        A rendered HTML template (index.html) for the main page of the application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection_response():
    """Handles the emotion detection request by analyzing the input text and returning 
    the emotional response.
    
    Extracts the text input from the query string, processes it through the emotion 
    detection model, and returns a formatted string with emotion scores and the dominant emotion.
    
    Returns:
        A string with emotion analysis results, including the individual emotion scores 
        and the dominant emotion.
        If no valid input is given or the detection fails, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

if __name__ == '__main__':
    app.run(debug=True)
