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

blob = TextBlob(Path("book_of_John_text.txt").read_text())

stops = stopwords.words("english")  

nouns = [w for w,pos in blob.tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') if w not in stops]
nouns = TextBlob(str(nouns))

items = nouns.word_counts.items() 

sorted_items = sorted(items, key = itemgetter(1), reverse=True)

top15 = sorted_items[:15]
top15 = str(top15)

#print(pd.DataFrame(top15, columns = ["word", "count"]))

mask = imageio.imread("mask_heart.png")

wc = WordCloud(colormap = "prism", mask = mask, background_color = "white")

wc = wc.generate(top15)

wc = wc.to_file("John.png")

