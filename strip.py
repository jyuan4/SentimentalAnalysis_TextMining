import re
import pickle
import string
import csv

# def stem(word):
#     for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
#         if word.endswith(suffix):
#             return word[:-len(suffix)]
#     return word

def stemmer(phrase):
	i=0
	while i < len(phrase):
		# print "index = ", i, "  , length = ", len(phrase)-1
		for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
			if phrase[i].endswith(suffix):
				# print "popping ", phrase[i]
				phrase.remove(phrase[i])
				i = i - 1
		
		i = i + 1
	return phrase

posWordArr = [posWord.rstrip('\n') for posWord in open('2006_positiveWords.txt')]
negWordArr = [negWord.rstrip('\n') for negWord in open('4783_negativeWords.txt')]
fpos = open('positiveWords.txt', 'w')
fneg = open('negativeWords.txt', 'w')

posWords = stemmer(posWordArr)
negWords = stemmer(negWordArr)

for j in posWords:
	fpos.write(j + '\n')

for j in negWords:
	fneg.write(j + '\n')




