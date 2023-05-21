import json
# This file was used to convert the simple dialogs.txt data into a intents.json type corpus.
# read the dataset from a file
with open('../FromChatGPT/dialogs.txt', 'r') as f:
  lines = f.readlines()

# create a list of intents
intents = []
for line in lines:
  # split the line into input and output
  input_text, output_text = line.strip().split('\t')
  # create an intent with a unique tag
  intent = {
    "tag": f"intent_{len(intents)}",
    "patterns": [input_text],
    "responses": [output_text]
  }
  intents.append(intent)

# create the intents data structure
intents = {
  "intents": intents
}

# serialize the intents data structure to JSON
intents_json = json.dumps(intents, indent=2)

# write the intents data structure to the intents.json file
with open('../FromChatGPT/intents.json', 'w') as f:
  f.write(intents_json)
















# # inputs, outputs = [], []
# # with open('dialogs.txt', 'r') as infile:
# #   for line in infile:
# #     input_text, output_text = line.strip().split('\t')
# #     print(input_text)
# #     print(output_text)
#
#
# import json
#
# # read the dataset from a file
# with open('dialogs.txt', 'r') as f:
#   lines = f.readlines()
#
# # create a list of intents
# intents = []
# for line in lines:
#   # split the line into input and output
#   input_text, output_text = line.strip().split('\t')
#   # create an intent with a unique tag
#   intent = {
#     "tag": f"intent_{len(intents)}",
#     "patterns": [input_text],
#     "responses": [output_text]
#   }
#   intents.append(intent)
#
# # create the intents data structure
# intents = {
#   "intents": intents
# }
#
# # serialize the intents data structure to a JSON string
# json_string = json.dumps(intents, indent=2)
#
# # write the JSON string to the output file
# with open('output.txt', 'w') as f:
#   f.write(json_string)
