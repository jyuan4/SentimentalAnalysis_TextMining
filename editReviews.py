import re
import pickle
import string
import csv


def splitString(line):
	# removing punctuation, making all lowercase, and spliting line into a list of words, called 'wordsInReview'
	line.translate(None, string.punctuation)
	myLine = line.translate(string.maketrans("",""), string.punctuation)
	lineLowerCase = myLine.lower()
	wordsInReview = lineLowerCase.split()	# split string into array

	return wordsInReview


def findAdj(wordsReview):
	i=0
	while i < len(wordsReview):
		for each in allWordsList:
			m = re.match(each + "*", wordsReview[i])
			if m:
				wordsReview[i] = each





fallComments = open('AllComments.csv','r')
posWordArr = [posWord.rstrip('\n') for posWord in open('positiveWords.txt')]
negWordArr = [negWord.rstrip('\n') for negWord in open('negativeWords.txt')]
allWordsList = posWordArr + negWordArr


line = fallComments.readline()
while line:
	wordsInReview = splitString(line)
	findAdj(wordsInReview)
	line = fallComments.readline()

