from nltk.corpus import wordnet

def obtenerSinonimos(palabra):
    sinonimos = []

    for syn in wordnet.synsets(palabra, lang='spa'):
        for name in syn.lemma_names('spa'):
            if(name != palabra):
                sinonimos.append(name)

    return set(sinonimos)



