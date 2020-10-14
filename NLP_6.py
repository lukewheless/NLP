from pathlib import Path
import nlp
import spacy 

nlp = spacy.load("en_core_web_sm")

doc1 = nlp(Path("RomeoAndJuliet.txt").read_text())
doc2 = nlp(Path("EdwardTheSecond.txt").read_text())

print(doc1.similarity(doc2)) #determines if author may be the same