from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the model and tokenizer
model_name = "your-model-name-here"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=200, do_sample=True, temperature=0.8)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

@app.route('/generate_text', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt')
    response = generate_response(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
