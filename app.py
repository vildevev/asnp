from flask import Flask
app = Flask(__name__)
import os
import openai

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".envrc"))

@app.route("/")
def home():
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get("OPEN_API_KEY")
    response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

    return response