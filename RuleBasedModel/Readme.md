
## Rule-Based Models

Rule-Based models are a fundamental approach in Natural Language Processing (NLP) that rely on a predefined set of linguistic rules and patterns to analyze and process text. These models aim to capture the inherent structure and grammar of the language by leveraging a set of handcrafted rules, regular expressions, and domain-specific knowledge. The rules define patterns or conditions that, when satisfied by the input text, trigger specific actions or outputs. Unlike machine learning-based models that learn patterns from data, Rule-Based models offer explicit control and interpretability, allowing developers to precisely define the desired behavior. By encoding linguistic and semantic rules, these models excel in tasks that require structured and rule-driven reasoning, such as named entity recognition, part-of-speech tagging, and syntactic parsing. While Rule-Based models may lack the flexibility to adapt to unseen patterns, they offer transparency and interpretability, making them a valuable tool in various NLP applications.

## How to use it ?

#### Method 1: Try on Google Colab

It is highly recommended that you first use the [Rule_Based_Bot.ipnyb](./Rule_Based_Bot.ipynb) jupyter notebook and try it on any of the online platform like  google Colab or Tensorflow Jupyter Notebook before setting up on your main machine to understand the code better.
This note book will explain the step by step process, with nice comments on how the actual process of model creation works and what steps you have to follow to build you final Chatbot model.

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
