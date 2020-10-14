from textblob import TextBlob

text = "Today is gonna be a good day!"

blob = TextBlob(text)

print(blob.sentences)

print(blob.words)

print(blob.tags)           #prints out word type

print(blob.noun_phrases)     #prints out noun statments   
        
print(round(blob.sentiment.polarity, 2))           #polarity = 0 is neutral
print(round(blob.sentiment.subjectivity, 2))

sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 5))         
    print(round(sentence.sentiment.subjectivity, 5))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())

print(blob.sentiment) #evaluates how pos vs neg statment is

sentences = blob.sentences

for sentence in sentences:
    print(sentence.sentiment)

print(blob.detect_language())

spanish = blob.translate(to="es")       #translate statement to spanish!

print(spanish)

from textblob import Word

index = Word("index")

print(index.pluralize())

animals = TextBlob('dog cat fish sheep bird').words

print(animals.pluralize()) #pluralizes words in blob

word = Word("theyr")

print(word.spellcheck())

print(word.correct())

#sentence = TextBlob("This sentence has misspelled wrds.")












