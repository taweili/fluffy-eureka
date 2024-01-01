from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "01-ai/Yi-6B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
with torch.device("cuda"):
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16)

inp = tokenizer(["Today I am in Paris and"], padding=True, return_tensors="pt").to("cuda")
res = model.generate(**inp, max_new_tokens=30)

print(tokenizer.batch_decode(res))
