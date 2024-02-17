from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import colorama
colorama.init()
from colorama import Fore, Style, Back
import random
import pickle

app = Flask(__name__)

# Load data from intents.json
with open("intents.json") as file:
    data = json.load(file)

# Load trained model and other objects
model = keras.models.load_model('chat_model')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# Parameters
max_len = 20

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([user_input]),
                                                                      truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    response = ""
    for i in data['intents']:
        if i['tag'] == tag:
            response = np.random.choice(i['responses'])

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
