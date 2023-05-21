
# Code for GPT 2  == 600 MB

from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the GPT-2 tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Load the GPT-2 model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Generate text
while True:
    input_text = input("User : ")
    if input_text != "kill":
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        output = model.generate(input_ids=input_ids,
                                max_length=500, do_sample=True)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print(generated_text)
    else:
        break
