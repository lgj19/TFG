from googletrans import Translator
from nltk.corpus import wordnet

def obtenerSinonimos(palabra):
    translator = Translator()
    word = translator.translate(palabra, src='es')

    sinonimos = []
    for syn in wordnet.synsets(word.text):
        for name in syn.lemma_names('spa'):
            sinonimos.append(name)

    return set(sinonimos)

obtenerSinonimos('total')