import nltk
import pandas as pd
import numpy as np


nltk.download('stopwords')
nltk.download('words')
nltk.download('wordnet')
nltk.download('averged_perception_tagger')
nltk.download('punkt')


sent=	"They	told	that	thier	eges	are	20	23	and	27	respectively"
add=[]
for word in sent.split():
    if word.isdigit():
        add.append(int(word))
print ("Ave", sum(add)/len(add))


from nltk.tokenize import word_tokenize, sent_tokenize
sent= "Hello all! how are you? Welcome to pun "
sent_tokenize(sent)
word_tokenize(sent)
from nltk.tokenize import SpaceTokenizer 

tk=SpaceTokenizer()
tk.tokenize(sent)

sent='Hello all!\tHow are u?\tto pune'
print(sent)
s1='ctas','catlike','catty','cat'
s2='stemmer','stemming','stemmed','stem'

s3='fishing','fished','fisher','fish'
from nltk.stem import PorterStemmer
ps=PorterStemmer()
ps.stem(s3[0])


for word in s4:
    ps=PorterStemmer()
    print(ps.stem(word))

# lemmatization
word='playing'
from nltk.stem import WordNetLemmatizer
wnl=WordNetLemmatizer()
print(wnl.lemmatize(word,'n')) # noun 3 print(wnl.lemmatize(word,'v')) # verb
print(wnl.lemmatize(word,'a')) # adjective 5 print(wnl.lemmatize(word,'r')) # adverb


word='went'
wnl=WordNetLemmatizer()
print(wnl.lemmatize(word,'n')) # noun 3 print(wnl.lemmatize(word,'v')) # verb
print(wnl.lemmatize(word,'a')) # adjective 5 print(wnl.lemmatize(word,'r')) # adverb
# POS tagging
from nltk import pos_tag
import nltk
nltk.download('averaged_perceptron_tagger')

sents='Rajgad (literal meaning Ruling Fort) is a hill fort situated in the Pune district of Maha)'
print(sents)
nltk.download('omw-1.4')

pos_tag(words)

tags=pos_tag(words)

for word in tags:
    if word[1].startswith('V'):
        print(word[0])

# spell correction
from textblob import TextBlob

t=TextBlob('computoor')
print(t.correct())

t=TextBlob('nead')
print(t.correct())


