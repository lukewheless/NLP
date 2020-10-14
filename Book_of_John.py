from pathlib import Path  
import imageio
from wordcloud import WordCloud
from textblob import TextBlob
import collections
import pandas as pd  

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

from operator import itemgetter 

#blob = TextBlob(Path("book_of_John_text.txt").read_text())
txt = open('book_of_John_text.txt', 'r')

stops = stopwords.words("english")  

nouns = [w for (w, pos) in TextBlob(txt).pos_tags if pos[0] == 'NN']

'''
for i in blob:
    if blob[i].tags == "NN":
        nouns = blob.word_counts.items() 
'''

items = [i for i in nouns if i[0] not in stops]

sorted_items = sorted(items, key = itemgetter(1), reverse=True)

top15 = sorted_items[:16]

print(pd.DataFrame(top15, columns = ["word", "count"]))


#wc = WordCloud().generate(top15)
#wc = wc.to_file("John.png")