'''This set of functions provides the deployment and
   server functionality for a flask app that analyze
   emotions in text
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# initiating flask application
app = Flask("Emotion Detector App")

@app.route('/emotionDetector')
def emotion_detect():
    '''This function when called as a HTTP GET
       uses flask requests to retrieve user input
       from javascript and uses the emotion_detector
       to analyze emotions and return a formatted string
    '''
    # retrieving the text from the UI and submitting it to the emotion detection module
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_response = emotion_detector(text_to_analyze)

    # Error handling invalid responses
    if emotion_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # utilizing an f string to output the response in the desired format
    return f"""For the given statement, the system response is 'anger': {emotion_response['anger']}
               , 'disgust': {emotion_response['disgust']}, 'fear': {emotion_response['fear']}
               , 'joy': {emotion_response['joy']} and 'sadness': {emotion_response['sadness']}. 
               The dominant emotion is <b>{emotion_response['dominant_emotion']}</b>."""

@app.route('/')
def render_index():
    '''This function renders the home index screen
    '''
    return render_template('index.html')    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)