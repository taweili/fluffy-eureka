import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("vivo-ai/BlueLM-7B-Chat", trust_remote_code=True, use_fast=False)
model = AutoModelForCausalLM.from_pretrained("vivo-ai/BlueLM-7B-Chat", device_map="cuda:0", torch_dtype=torch.bfloat16, trust_remote_code=True)
model = model.eval()
inputs = tokenizer("[|Human|]:三国演义的作者是谁？[|AI|]:", return_tensors="pt")
inputs = inputs.to("cuda:0")
pred = model.generate(**inputs, max_new_tokens=64, repetition_penalty=1.1)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
