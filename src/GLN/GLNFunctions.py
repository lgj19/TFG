from nltk.corpus import wordnet
import os
import openai 

def obtenerSinonimosGPT3(palabra):
    # Load your API key from an environment variable or secret management service
    openai.api_key = "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"

    response = openai.Completion.create(engine="text-davinci-002",
    prompt='''Sugiere 5 o menos sinónimos en español,
     separados por comas
     y que no se repitan para la palabra {}'''.format(palabra),
     temperature=0.7, max_tokens=100)
    return response.choices[0].text[2:] + ".\n"


def obtenerSinonimos(palabra):
    sinonimos = []

    for syn in wordnet.synsets(palabra, lang='spa'):
        for name in syn.lemma_names('spa'):
            if(name != palabra):
                sinonimos.append(name)

    return set(sinonimos)
