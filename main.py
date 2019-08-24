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
#user_file = input('Enter the filename.ext: ')   # Uncomment line @ end of prj
user_file = 'sample.txt'                         # Del line @ end of project

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

# (7) close the file
infile.close()


'''
                   (2) PROCESS WORDS ONLINE

## LOOP THROUGH WORD LIST
# (1) Request (get) webpage using word from user's file // response_obj
# (2) Check status of webpage
# (3) Transfer page into an parser object  // bs4_object
# (4) Parse and retireve data // string elements_2D_list
#       4.1) English-definition, Hanzi
# (5) CALL # (3) OUTPUT TO FILE
'''


'''
                   (3) OUTPUT TO FILE

# (1) Create a file for writing
# (2) Write the data as a record into the list: original word(s)
# (3) Write the data as a record into the list: parsed English-def, Hanzi
# (4) Close the file
'''

# Call the main function
#main()
