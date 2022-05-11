import os
import string

def fileReader(file):
    openFile = open(os.getcwd() + file, 'r')
    fileAsList = openFile.readlines()
    openFile.close()

    return fileAsList

def fileWordCleaner(file):
    listLines = fileReader(file)

    print('UNCLEAN', listLines)

    for index in range(len(listLines)):
       listLines[index] = listLines[index].translate(str.maketrans('', '', string.punctuation))
       listLines[index] = listLines[index].replace('\n', '')

    print('CLEANED', listLines)

def fileStringComparison(file):
    listLines = fileReader(file)

    print('String list to search', listLines)

    searchString = 'MA'

    for index in range(len(listLines)):
        if searchString in listLines[index]:
            print('String with substring ' + searchString + ': ', listLines[index])

file = '/challenges/cookie.txt'

fileWordCleaner(file)
fileStringComparison(file)
