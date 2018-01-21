import re
import pickle
import string
import csv

def splitString(line):
    # remove punctuation and split line into a list of words
    line.translate(None, string.punctuation)
    myLine = line.translate(string.maketrans("",""), string.punctuation)
	
    # make all lowercase
    lineLowerCase = myLine.lower()

    # split string into array
    wordsInReview = lineLowerCase.split()	

	return wordsInReview

def parseAdj(wordsInReview):
    # find adjectives within review
    adjectives = [x for x in allWordsList if x in wordsInReview]

    # add adjectives to list without repeats
    for element in adjectives:
        if element not in allAdjList:
            allAdjList.append(element)

## Open the file with read only permit
fAllComments = open('AllComments.csv','r')

## store all positive words into list
posWordArr = [posWord.rstrip('\n') for posWord in open('positiveWords.txt')]
## store all negative words into list
negWordArr = [negWord.rstrip('\n') for negWord in open('negativeWords.txt')]
## combine positive and negative lists into one list
allWordsList = posWordArr + negWordArr

## create list
allAdjList = []

## Read the first line
line = fAllComments.readline()
while line:
    wordsInReview = splitString(line)
    parseAdj(wordsInReview)
    line = fAllComments.readline()

print allAdjList

fAllComments.close()
