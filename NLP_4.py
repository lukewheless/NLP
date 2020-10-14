import spacy 

#nlp = spacy.load("en")

nlp = spacy.load("en_core_web_sm")

d = nlp("In 1994, Tim Berner-Lee founded the Worldwide Web Consortium (W3C), devoted to the developing web tech")

for en in d.ents:
    print(en.text, ":", en.label_)







