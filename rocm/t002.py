# https://github.com/ROCm/ROCm/issues/2536

from transformers import *
pipe = pipeline("translation", "Helsinki-NLP/opus-mt-en-zh", device=1)

for i in range(100):
    ret = pipe("I am bear and Bear likes Beer")
    print(ret)
