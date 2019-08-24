#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Cantonese Dictionary
# Description:
#     Creates a Cantonese dictionary.
# Date: 2019/08/23
# Revised:
#     <revision date>

# list libraries used
import bs4, requests, webbrowser

# Declare global constants

#def main():

'''
                        BLUEPRINT

# (1) GET USER-DEFINED FILE
# (2) PROCESS WORDS ONLINE
# (3) OUTPUT TO FILE
'''

'''
                   (1) GET USER-DEFINED FILE

# (1) get filename.ext // string var
# (2) open the file    // file_obj var
# (3) read first record's description field // string orig_words[]
# (4) strip the '\n' && ',' from the description
# (5) close the file
'''
# (1) Get the filename from user
#user_file = input('Enter the filename.ext: ')  # Uncomment line @ end of prj
#user_file = 'sample.txt'                       # Del line @ end of project
user_file = 'sample2.txt'                       # del after project completion

# (2) Open the file for reading
infile = open(user_file, 'r')

# (3) Read the first record's description field
lines = infile.readlines()

# (4) strip the ',' and '\n' from the description
nLines = len(lines)
for i in range(nLines):
    lines[i] = lines[i].rstrip('\n')
    if (',' in lines[i]):
        lines[i] = lines[i].rstrip(',')

#DEBUG = PASS
for i in range(nLines):
    print(lines[i])

# (5) close the file
infile.close()


'''
                   (2) PROCESS WORDS ONLINE

# (1) Request (get) webpage using word from user's file // response_obj
# (2) Check status of webpage
# (3) Transfer page into an parser object  // bs4_object
# (4) Parse and retireve data // string elements_2D_list
#       4.1) English-definition, Hanzi
'''


# (1) Request (get) web page
res = []  # response objects
soup = [] # soup objects

for i in range(nLines):
    # Init query for web address
    address = lines[i]
    address = address.replace(" ", "+")
    # Request the web page and store inside a response object
    response = requests.get('http://cantonese.org/search.php?q=' + address)

    # (2) Check status of webpage
    if (response.raise_for_status()):
        # Store response object inside a response list
        res[i].append(response)

        ##DEBUG = ------------------------------------------------FAIL
        print(res[i])

        # (3) Create a BeautifulSoup object in a bs4 list
        soup[i].append = bs4.BeautifulSoup(res[i].text, features="html_parser")

    #DEBUG = PASS
    #print('http://cantonese.org/search.php?q=', address, sep='')
    #webbrowser.open('http://cantonese.org/search.php?q=' + address)

# End for


# (4) Parse and retireve data // string elements_2D_list
# Declare variables
lenRows = len(res)
print(lenRows)
lenCols = 2
elems = []  # HTML element objects
#hanzi = ''
#definition = ''
#roman = ''

##DEBUG = PASS
print('Parsing Data -- Declared vars --')

# Get parsed data and store them in elems[]
for i in range(lenRows):

    ##DEBUG = ------------------------------------------------FAIL
    print('HELP!')

    # get hanzi, definition, romanization from web page
    roman = soup[i].select('.resulthead strong')
    definition = soup[i].select('.resultbody p')
    hanzi = soup[i].select('.resulthead')

    ##DEBUG = ------------------------------------------------FAIL
    print('HELP!')

    # store hanzi, definition, romanization from web page
    elems[i][0].append(roman)
    elems[i][1].append(definition)
    elems[i][2].append(hanzi)

    ###DEBUG = ~
    print('INSIDE GET DATA')
    print(elems)

# End for

'''
                   (3) OUTPUT TO FILE

# (1) Create a file for writing
# (2) Write the data as a record into the list: original word(s)
# (3) Write the data as a record into the list: parsed English-def, Hanzi
# (4) Close the file
'''

# Call the main function
#main()
