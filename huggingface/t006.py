#
# https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
# 

from llama_cpp import Llama

model_path = "models/dolphin-2.6-mistral-7b-dpo.Q4_K_M.gguf"

print("loading llm")
# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path=model_path,  # Download the model file first
  n_ctx=2048,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=0        # The number of layers to offload to GPU, if you have GPU acceleration available
)

print("llm ready...")

output = llm(
      "Q: Name all planets in the solar system? A: ", # Prompt
      max_tokens=1024, # Generate up to 32 tokens
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion

print("llm output")

print(output)
