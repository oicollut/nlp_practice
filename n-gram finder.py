import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import *
import pandas
import numpy
import xlsxwriter

raw_data =  pandas.read_excel('trail_data1.xlsx')#the file is a list of prompt sand completions
not_so_raw_data1 = raw_data['completion'].tolist()#converting all completions to a list
not_so_raw_data2 = str(not_so_raw_data1)#converting completions to string for tokenization
tokens = word_tokenize(not_so_raw_data2)#making the text into a list of tokens (all the words in a list)
#print(tokens)
stops = set(stopwords.words('english'))#filtering out NLTK's inbuilt stopwords
clean_tokens = []
for word in tokens:
   if word not in stops and word.isalnum():
        clean_tokens.append(word)

tags = nltk.pos_tag(clean_tokens)#creating list where all words are tagged with their part of speech code letters: [('The', 'DT'), ('Tahoe', 'NNP'), ('Rim', 'NNP'), ('Trail', 'NNP')]
#print(tags[:10])

#_____________BIGRAMS_____________
bigram_measures = nltk.collocations.BigramAssocMeasures()#calling the bigram function to find all bigrams and put them into a list

finder = BigramCollocationFinder.from_words(tags)#extracting bigrams from TAGGED LIST
finder.apply_freq_filter(3)
bigrams = finder.nbest(bigram_measures.pmi, 100000)#final variable storing the best bigrams by pmi out of the staten number of bigrams

#JJN BIGRAMS________________________________
"""tagged_jjn_bigrams = []#putting only the adjective + noun bigrams into a list for further cleaning. Goal is to produce a list of bigrams with no other tags.
for pair in bigrams[:10000000]:
        if ("JJ" in pair[0]) and ('NNP' or "NNS" or "NN" in pair[1]):
          tagged_jjn_bigrams.append(pair)



messy_jjn_bigrams = []#temporary list we need for our multistep nested tuple and tag removal process
jjn_bigrams = []

stoplist = ["JJ", "JJR", "JJS", 'NNP', "NNS", "NN"]

for a, b in tagged_jjn_bigrams:#getting rid of extra nesting
        messy_jjn_bigrams.append(a + b)
for tup in messy_jjn_bigrams:#getting rid of tags
        newtup = (tup[0] + " " + tup[2])
        jjn_bigrams.append(newtup)#final NORMAL list of 2-word adj + noun collocations
        

print(jjn_bigrams)"""


#_____________________TRIGRAMS_________________________
"""trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(tags)#extracting bigrams from TAGGED LIST
finder.apply_freq_filter(1)
trigrams = finder.nbest(trigram_measures.pmi, 1000000)#final variable storing the best bigrams by pmi out of the staten number of bigrams

#print(trigrams)


NNP_tagged_trigrams = []#putting only the adjective + noun bigrams into a list for further cleaning. Goal is to produce a list of bigrams with no other tags.
for pair in trigrams[:1000000]:
        if ("NNP" in pair[0]) and ('NNP' in pair[1]) and ('NNP' in pair[2]):
          NNP_tagged_trigrams.append(pair)
#print(NNP_tagged_trigrams)


messy_trigrams = []#temporary list we need for our multistep nested tuple and tag removal process
clean_trigrams = []

for a, b, c in NNP_tagged_trigrams:#getting rid of extra nesting
        messy_trigrams.append(a + b + c)
for tup in messy_trigrams:#getting rid of tags
        newtup = (tup[0] + " " + tup[2] + " " + tup[4])
        clean_trigrams.append(newtup)#final NORMAL list of 2-word adj + noun collocations
        

print(clean_trigrams)"""

