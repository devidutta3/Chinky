import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "models/Qwen2.5-7B-Instruct"

print("Loading Chinky's Qwen model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Model loaded!")
print("Device:", next(model.parameters()).device)

message = "Hello Chinky, introduce yourself in one sentence."

messages = [
    {"role": "system", "content": "You are Chinky, a friendly personal AI assistant."},
    {"role": "user", "content": message}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=50
    )

response = tokenizer.decode(
    outputs[0][inputs["input_ids"].shape[1]:],
    skip_special_tokens=True
)

print("\nChinky:", response)