from textblob import TextBlob
from pathlib import Path

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())
'''
print(blob.words.count("joy"))
print(blob.noun_phrases.count("lady capulet"))

'''
from textblob import Word

happy = Word("happy")

print(happy.definitions)

print(happy.synsets)
















