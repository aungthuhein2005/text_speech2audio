from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import re

app = Flask(__name__)

# Path to save the audio file (change this to your actual Downloads folder path)
DOWNLOAD_PATH = os.path.expanduser('~/Downloads')

def sanitize_filename(text):
    # Remove any invalid characters for filenames
    return re.sub(r'[^\w\-_\. ]', '_', text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    # Get the Japanese word from the form input
    text = request.form['text']
    
    # Sanitize the input to create a valid filename
    file_name = sanitize_filename(text) + '.mp3'
    file_path = os.path.join(DOWNLOAD_PATH, file_name)
    
    # Generate the TTS audio in Japanese
    tts = gTTS(text, lang='ja')
    
    # Save the audio file in the Downloads folder
    tts.save(file_path)

    # Return the file for download
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
