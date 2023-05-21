# Code for google/flan-t5-base -- 970 MB


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the T5 tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

# Load the T5 model
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")


# Generate text using the T5 model
while True:
    input_text = input("User : ")
    if input_text != "kill":
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        output_ids = model.generate(input_ids)
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        print(output_text)
    else:
        break
