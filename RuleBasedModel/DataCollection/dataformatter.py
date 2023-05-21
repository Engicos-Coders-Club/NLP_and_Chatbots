# To give Random tags for the tag data format file.

import json
import random

# Define the new tags that you want to use
new_tags = ["greeting", "joke", "weather", "mood", "hobbies", "favorites", "education", "sports", "movies", "music"]

# Read the intents from the file
with open("intents.json", "r") as f:
    intents = json.load(f)

# Update the tags of each intent to a random new tag
for intent in intents["intents"]:
    intent["tag"] = random.choice(new_tags)

# Write the updated intents back to the file
with open("intents.json", "w") as f:
    json.dump(intents, f, indent=4)






'''
# To remove all the punctuation marks from the data i downloaded dialogs.txt

import re

# Open the input file
with open("Data/dialogs.txt", "r") as f:
    data = f.readlines()

# Create a list to store the first sentences
first_sentences = []

# Loop through each line of the input file
for line in data:
    # Split the line into two sentences
    sentences = line.strip().split("\t")

    # Extract the first sentence
    first_sentence = sentences[0]

    # Remove any periods and quotation marks from the sentence
    first_sentence = re.sub("[.\"\'\,]", "", first_sentence)

    # Add the sentence to the list of first sentences
    first_sentences.append(f'"{first_sentence}",')

# Write the first sentences to the output file
with open("Data/output.txt", "w") as f:
    f.write("\n".join(first_sentences))

# with open("dialogs.txt", "r") as input_file:
#     with open("output.txt", "w") as output_file:
#         for line in input_file:
#             first_sentence = line.split("\t")[0]
#             output_file.write(f'"{first_sentence}",\n')


'''











'''
#Code to use NLTK to give tags based on the pattern of questions

import nltk
import json
from nltk import word_tokenize, pos_tag
from collections import Counter

# Load the intents from the intents.json file
with open('DataCollection/intents.json') as f:
    intents = json.load(f)

# Define a function that takes a list of words as input and returns a list of named entities
def extract_entities(text):
    entities = []
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        if tag == 'NNP':
            entities.append(word)
    return entities

# Loop through the intents and extract named entities from the patterns
for intent in intents['intents']:
    if isinstance(intent.get('patterns', ''), str):
        intent['patterns'] = [intent['patterns']]
    for pattern in intent['patterns']:
        entities = extract_entities(pattern)
        if entities:
            intent['tag'] = ' '.join(entities)
    else:
        intent['tag'] = 'Other'

# Get a list of all the tags in the intents
all_tags = [intent['tag'] for intent in intents]

# Get a list of the most common tags
most_common_tags = [item[0] for item in Counter(all_tags).most_common()]

# Assign the most common tags to their respective intents
for intent in intents:
    if intent['tag'] in most_common_tags[:5]:
        intent['tag'] = intent['tag']
    else:
        intent['tag'] = 'Other'

# Save the modified intents to a new file
with open('intents_with_tags.json', 'w') as f:
    json.dump(intents, f)




'''

