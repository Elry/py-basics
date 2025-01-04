import os
import string

def file_reader(file):
    open_file = open(os.getcwd() + file, 'r')
    file_as_list = open_file.readlines()
    open_file.close()

    return file_as_list

def file_word_cleaner(file):
    list_lines = file_reader(file)

    print('UNCLEAN', list_lines)

    for index in range(len(list_lines)):
       list_lines[index] = list_lines[index].translate(str.maketrans('', '', string.punctuation))
       list_lines[index] = list_lines[index].replace('\n', '')

    print('CLEANED', list_lines)

def file_string_comparison(file):
    list_lines = file_reader(file)

    print('String list to search', list_lines)

    search_string = 'MA'

    for index in range(len(list_lines)):
        if search_string in list_lines[index]:
            print('String with substring ' + search_string + ': ', list_lines[index])

file = '/challenges/cookie.txt'

file_word_cleaner(file)
file_string_comparison(file)
