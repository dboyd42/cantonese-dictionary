#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Cantonese Dictionary
# Description:
#     Creates a Cantonese dictionary.
# Date: 2019/08/23
# Revised:
#     <revision date>

# list libraries used
import bs4, requests
# import webbrowser     # not used yet

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
# if argv -> determine '.' file_obj or word list sep by ','
# if argv == 0 THEN
print('\n\n')
choice_word = input('Enter <filename.ext> or word1, word2: ')
print('\n\n')
#choice_word = "zao an"   # Test word
# create for loop to enter multiple words sep by ','
lines = []
lines.append(choice_word)
# remove ',' delimeter
#lines[0] = lines[0].rstrip(',')



# then get file and yada yada yada
# if ('.' is in choice_word): 
# (1) Get the filename from user
#user_file = input('Enter the filename.ext: ')  # Uncomment line @ end of prj
#user_file = 'sample.txt'                       # Del line @ end of project
#user_file = 'sample2.txt'                      # del after project completion

#
## (2) Open the file for reading
#infile = open(user_file, 'r')
#
## (3) Read the first record's description field
#lines = infile.readlines()

# (4) strip the ',' and '\n' from the description
nLines = len(lines)
#for i in range(nLines):
#    lines[i] = lines[i].rstrip('\n')
#    if (',' in lines[i]):
#        lines[i] = lines[i].rstrip(',')

#DEBUG(PRINT USER FILE) = PASS
#for i in range(nLines):
#    print(lines[i])

# (5) close the file
#infile.close()

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
    if (response.ok):
        # Store response object inside a response list
        res.append(response)

        # (3) Create a BeautifulSoup object in a bs4 list
        soup.append(bs4.BeautifulSoup(res[i].text, features="html.parser"))

# End for

# (4) Parse and retireve data
lenRows = len(res)
hanzi = []
definition = []
roman = []

# Get parsed data and store them in elems[]
for i in range(lenRows):

    # get and store hanzi, definition, romanization from web page
    roman.append(soup[i].select('.resulthead strong'))
    try:
        definition.append(soup[i].select('.defnlist li')[0])
    except IndexError:
        try:
            definition.append(soup[i].select('.resultbody')[0])
        except:
            definition.append('null')
    #definition.append(soup[i].select('.defnlist li'))
    hanzi.append(soup[i].select('.resulthead'))

# End for

'''
                   (3) OUTPUT TO FILE


# (1) Create a file for writing
# (2) Write the data as a record into the list: original word(s)
# (3) Write the data as a record into the list: parsed English-def, Hanzi
# (4) Close the file
'''

# Display to terminal
try:
    rom = roman[i][0].getText()
except:
    rom = lines[i]
try:
    define = definition[i].getText()
except:
    #define = ' '
    print('NOT FOUND: Line#', str(i), ': ', str(lines[i]), sep='')
    define = definition[i][0]
    #notFound_file.write('Line #' +  str(i) + ',' + lines[i] + '\n')

print(rom, ', ', define, ', ', sep='', end='\n')



# (1) Create a file for writing
#outfile = open('canto-definitions.csv', 'w')
# notFound_file = open('canto-not-defined.csv', 'w')
# not_defined = []

# (2) Write the data to the outfile
#for i in range(lenRows):
    # BUG: Hanzi is outputting wrong characters-------------------------------!
    #    : -> Tried on LibreOffic, gEdit, Vim (Linux Platform)----------------!
    #    : :: Possible Cause: Encoding Issues---------------------------------!
    #    : ::       ==> (Linux? bs4?)-----------------------------------------!
    # (1): -> Uncomment and open with Excel, Notepad, Etc (Windows Platform)--!
    # (2): -> bs4 selector options (encoding, etc)----------------------------!
    # https://stackoverflow.com/questions/15056633/python-find-text-using-beautifulsoup-then-replace-in-original-soup-variable

    #outfile.write(roman[i][0].getText() + ',' + definition[i].getText() + \
                  #',' + '\n')
                  #',' + hanzi[i][0].getText() + '\n')
#    try:
#        rom = roman[i][0].getText()
#    except:
#        rom = lines[i]
#    try:
#        define = definition[i].getText()
#    except:
#        define = ' '
#        print('NOT FOUND: Line#', str(i), ': ', lines[i], sep='')
#        notFound_file.write('Line #' +  str(i) + ',' + lines[i] + '\n')
#
#    outfile.write(rom + ',' + define + ',' + '\n')


# (3) Close the file
#outfile.close()
#notFound_file.close()
# Call the main function
#main()
