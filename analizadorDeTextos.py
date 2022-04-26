import stanza;

nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos')
doc = nlp('''
          El Valencia Basket logró imponerse en el Buesa Arena al Bitci Baskonia por 71 a 78,
          en un encuentro en el que llegaron a disfrutar de 20 puntos de ventaja en el inicio del
          segundo cuarto, con un final que acabaría en 7 puntos de diferencia en el marcador.
          La mayor rotación y
          frescura física de los valencianos acabó siendo decisiva, así como la aportación de
          López-Aróstegui y Hermannsson. Entre ambos anotaron 45 de los 78 puntos en total.
          El vizcaíno acabaría con 20 puntos y 24 de valoración, mientras que el islandés firmó 15 puntos
          y 6 asistencias. Por parte del otro equipo, el más productivo fue Baldwin con 15 de valoración,
          disputando 23 minutos en la cancha.
          ''')

print("\nAnálisis sintáctico del texto:\n")
print(*[f'word: {word.text}\tupos: {word.upos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')


nlp = stanza.Pipeline(lang='es', processors='tokenize,ner')
doc = nlp('''
          El Valencia Basket logró imponerse en el Buesa Arena al Bitci Baskonia por 71 a 78,
          en un encuentro en el que llegaron a disfrutar de 20 puntos de ventaja en el inicio del
          segundo cuarto, con un final que acabaría en 7 puntos de diferencia en el marcador.
          La mayor rotación y
          frescura física de los valencianos acabó siendo decisiva, así como la aportación de
          López-Aróstegui y Hermannsson. Entre ambos anotaron 45 de los 78 puntos en total.
          El vizcaíno acabaría con 20 puntos y 24 de valoración, mientras que el islandés firmó 15 puntos
          y 6 asistencias. Por parte del otro equipo, el más productivo fue Baldwin con 15 de valoración,
          disputando 23 minutos en la cancha.
          ''')

print("\nLista de entidades del texto:\n")
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')