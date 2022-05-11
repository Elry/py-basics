import string
import os

def words(file):
    openFile = open(os.getcwd() + '/challenges/' + file, 'r')
    listLines = openFile.readlines()

    print('UNCLEAN', listLines)

    for index in range(len(listLines)):
       listLines[index] = listLines[index].translate(str.maketrans('', '', string.punctuation))
       listLines[index] = listLines[index].replace('\n', '')

    print('CLEANED', listLines)

    openFile.close()

words('cookie.txt')