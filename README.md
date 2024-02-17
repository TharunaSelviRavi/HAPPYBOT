# Simple Chatbot with TensorFlow and Keras

## Overview
This repository contains code for a simple chatbot implemented using TensorFlow and Keras. The chatbot is trained on a dataset of intents and responses, allowing it to generate appropriate responses based on user input.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Files and Directories](#files-and-directories)
- [Training the Model](#training-the-model)

## Prerequisites
tensorflow==2.3.1   
nltk==3.5   
colorama==0.4.3   
numpy==1.18.5  
scikit_learn==0.23.2   
Flask==1.1.2   


You can install the required packages using the following command:  
       pip install -r requirements.txt

# Usage
   Clone the repository:  
          git clone https://github.com/TharunaSelviRavi/HAPPYBOT.git  
          cd HAPPYBOT  

   Run the chatbot in the console:   
         python chat.py   
   You can start interacting with the chatbot by typing messages. Type "quit" to exit the chat.   
   Alternatively, deploy the chatbot as a Flask web application:   
       python app.py    
   Open your web browser and navigate to http://localhost:5000 to use the chatbot through a simple web interface.

# Files and Directories
   chatbot.py: Script for running the chatbot in the console.  
   app.py: Flask web application for using the chatbot through a web interface.  
   intents.json: Dataset containing intents and responses.  
   chat_model/: Directory containing the saved trained model.  
   tokenizer.pickle: Pickle file for the fitted tokenizer.  
   label_encoder.pickle: Pickle file for the fitted label encoder.  
   requirements.txt: List of required Python packages.  

# Training the Model
    If you want to retrain the model or make changes to the training process:
        Modify the intents.json file with your own intents and responses.
        Run the training script:
             python train.py
