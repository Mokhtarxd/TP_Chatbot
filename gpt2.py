from transformers import GPT2LMHeadModel, GPT2Tokenizer
# Charger le modèle GPT-2 et le tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# Fonction pour générer une réponse
def generate_response(input_text):
 inputs = tokenizer(input_text, return_tensors="pt")
 outputs = model.generate(
  inputs.input_ids,
  attention_mask=inputs.attention_mask,
  pad_token_id=tokenizer.eos_token_id,
  max_length=50,
  num_return_sequences=1
 )
 response = tokenizer.decode(outputs[0], skip_special_tokens=True)
 return response
# Tester le chatbot
user_input = "Bonjour, chatbot!"
print(generate_response(user_input))