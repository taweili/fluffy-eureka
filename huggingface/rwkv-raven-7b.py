import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH="RWKV/rwkv-raven-7b"
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16).to(0)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

prompt = "\n北京有天安门，上海有"

inputs = tokenizer(prompt, return_tensors="pt").to(0)
output = model.generate(inputs["input_ids"], max_new_tokens=400)
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
