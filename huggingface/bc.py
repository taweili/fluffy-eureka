import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig

model_name="baichuan-inc/Baichuan2-7B-Chat"

tokenizer = AutoTokenizer.from_pretrained(model_name, 
                                          use_fast=False, 
                                          trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, 
                                             device_map="auto", 
                                             torch_dtype=torch.bfloat16, 
                                             trust_remote_code=True)
model.generation_config = GenerationConfig.from_pretrained(model_name)
messages = []
messages.append({"role": "user", "content": "解释一下“温故而知新”"})
response = model.chat(tokenizer, messages)
print(response)

