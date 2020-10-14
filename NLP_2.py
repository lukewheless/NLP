import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

from textblob import TextBlob

stops = stopwords.words("english")
'''
print(stops)

blob = TextBlob("today is a beautiful day.")

new_blob = [word for word in blob.words if word not in stops]
print(new_blob)


for i in blob:
    for j in stopwords:
        if stopwords[j] == blob[i]:
            new_blob.append(blob[i])
'''
from textblob import TextBlob
from pathlib import Path

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

items = blob.word_counts.items()    #tuple with every word and number it occurrs

items = [i for i in items if i[0] not in stops] #does same thing but removes unnecessary words like the

print(items)

from operator import itemgetter 

sorted_items = sorted(items, key = itemgetter(1), reverse=True)

top20 = sorted_items[:21]













