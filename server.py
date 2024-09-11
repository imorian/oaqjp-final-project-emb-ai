"""
This module implements a Flask application to analyze emotions from text input using the EmotionDetection library.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_function():
    """
    Receives text input from the user via POST request,
    processes it using the emotion_detector function, and returns a formatted response.
    """
    text_to_analyze = request.form.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = (f"For the given statement, the system response is 'anger': "
                         f"{response['anger']}, 'disgust': {response['disgust']}, "
                         f"'fear': {response['fear']}, 'joy': {response['joy']}, "
                         f"and 'sadness': {response['sadness']}. The dominant emotion is "
                         f"{response['dominant_emotion']}.")

    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the index.html page, which contains the input form for text analysis.
    """
   
