from flask import Flask
app = Flask(__name__)
import os
import openai

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".envrc"))
openai.api_key = os.environ.get("OPEN_API_KEY")

@app.route("/")
def home():
    f = open('recording.txt','r')
    prompt = f'Suggest several questions to ask each other next based on the conversation between these people: {f}'
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)
    return response

@app.route("/record")
def record():
    audio_file= open("recording.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    file = open('recording.txt', 'w')
    file.write(transcript["text"])
    file.close()
    return transcript