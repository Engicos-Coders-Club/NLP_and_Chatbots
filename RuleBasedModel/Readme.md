# Rule Based Model

bring some theory from chatGPT

## How to use it ?

#### Method 1: Try on Google Colab

It is highly recommended that you use the [Rule_Based_Bot.ipnyb](./Rule_Based_Bot.ipynb) jupyter notebook and try it on any of the online platform like  google Colab or Tensorflow Jupyter Notebook.
This note book will explain the step by step process, with the nice comments on how the actual process of model creation works and what steps you have to follow to build you final Chatbot model.

#### Method 2 : Setup on you Local Machine

Follow the below steps to setup the workflow on your local machine. It is reccomended that you use Python 3.8.

1. Create a virtual Environment. (This step is not cumpulsory, but it is good practice, to keep you main python installation clean and easily revert back if anythin goes wrong)

> Run : ```Python -m venv venv```

> Then run : ```.\venv\Scripts\activate```

2. Make sure you are in the RuleBasedModel directory

> Run : ```cd RuleBasedModel\```

3. Install the requirements

> Run : ```pip install -r requirements.txt```

4. Now to train the chatbot

> Run : ```python Train.py```

This should create the a `chat_model` directory containing the model and two files `label_encoder.pickle` and `tokenizer.pickle`, which contains the configurations for your specific machine.

5. Now you can use the model using the code from the Test.py

> Run : ```python Test.py``

6. And thats it!
   Depending on the data you will use in the `intents.json` file and by changing the configurations in training file, you will get the desired model.
