

# Import the model class and the tokenizer
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration


# Download and setup the model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained(
    "facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained(
    "facebook/blenderbot-400M-distill")


while True:
    utterance = input("User : ")
    if utterance != "kill":
        inputs = tokenizer(utterance, return_tensors="pt")
        res = model.generate(**inputs)
        print(tokenizer.decode(res[0]))
    else:
        break
