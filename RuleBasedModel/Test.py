
# TODO : this is the most shitiest model i have ever seen, now it is giving output becouase for example wheter tag is given to thousands of lines and it prints all the lines matching. Now either you find out how to print best of those lines or use some other machine learning technique since even changing data not going to help.

import json
import numpy as np
from tensorflow import keras
# from sklearn.preprocessing import LabelEncoder

import colorama

colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat():
    # load trained model
    model = keras.models.load_model('chat_model')
    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    # parameters
    max_len = 20
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "kill":
            break
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, np.random.choice(i['responses']))
        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))


print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()