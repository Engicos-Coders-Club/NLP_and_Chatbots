import re

# Open the input file
with open("dialogs.txt", "r") as f:
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
with open("output.txt", "w") as f:
    f.write("\n".join(first_sentences))

# with open("dialogs.txt", "r") as input_file:
#     with open("output.txt", "w") as output_file:
#         for line in input_file:
#             first_sentence = line.split("\t")[0]
#             output_file.write(f'"{first_sentence}",\n')
