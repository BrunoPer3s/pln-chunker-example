import spacy
nlp = spacy.load("pt_core_news_sm")
sentence = "Emma Watson postou uma foto com Daniel Radcliffe."
doc = nlp(sentence)
for chunk in doc.noun.chunks:
    print(chunk.text)