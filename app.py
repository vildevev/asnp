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
    prompt = f'Suggest multiple things to talk about next based on this conversation: {f}'
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response["text"]
    file = open('recording_response.txt', 'w')
    file.write(transcript["text"])
    file.close()

    return response

@app.route("/record")
def record():
    audio_file= open("recording.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    file = open('recording.txt', 'w')
    file.write(transcript["text"])
    file.close()
    return transcript

@app.route("/format")
def format():
    # TODO: read from open API response
    # TODO: do this realtime
    response = "\n\n1. What other hobbies do you have?\n2. What do you like to do in your free time?\n3. What do you think about the current state of the world?\n4. What do you think are the biggest challenges facing society today?\n5. What do"
    return response