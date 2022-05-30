import os
import openai 

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

response = openai.Completion.create(engine="text-davinci-002",
 prompt="Sugiere 5 o menos sinónimos en español, separados por comas y que no se repitan para la palabra intempestivo", temperature=0.7, max_tokens=50)
print(response.choices[0].text)