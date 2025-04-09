"""Flask server for emotion detection API."""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze emotion in given text and return formatted response."""
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400
    
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400
    
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)