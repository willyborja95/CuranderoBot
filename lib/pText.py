import spacy

nlp = spacy.load('es')

def tokeniza(text):
    lista=[]
    doc = nlp(u""+text)
    for token in doc:
        lista.append(token.lemma)
    return lista
    
