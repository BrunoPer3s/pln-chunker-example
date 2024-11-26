import spacy
nlp = spacy.load("pt_core_news_sm")
sentence = "Emma Watson postou uma foto com Daniel Radcliffe no Instagram, mas a imagem foi removida."
doc = nlp(sentence)
for chunk in doc.noun_chunks:
    print(chunk.text)