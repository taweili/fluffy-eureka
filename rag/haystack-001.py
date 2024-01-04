from haystack.components.generators import GPTGenerator

gg = GPTGenerator(api_base_url="http://localhost:8000/v1",
                    model_name="mistral",
                    api_key="xxx")

response = gg.run("Why is sky blue?");

print(response)
