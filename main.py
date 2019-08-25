#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Cantonese Dictionary
# Description:
#     Creates a Cantonese dictionary.
# Date: 2019/08/23
# Revised:
#     2019/08/24

# list libraries used
import bs4, requests
# import webbrowser     # not used yet

# Declare global constants

def main():

    # Declare vars
    user_file = ''  # str filename
    lines   = []  # str lines from file
    t_def   = []  # str Terms' definition
    t_hanzi = []  # str Terms' Hanzi
    t_roman = []  # str Terms' romanization

    #user_file = "sample.txt"
    #user_file = "sample2.txt"
    #user_file = "sample3.txt"

    # Get user-defined file
    user_file = input('Enter the filename.ext: ')  # Uncomment line @ end of prj
    lines = get_file(user_file)

    # Process words online
    t_def, t_hanzi, t_roman = process_lines(lines)

    # Output to file
    write_file(lines, t_def, t_hanzi, t_roman)


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
#print('\n\n')
#choice_word = input('Enter <filename.ext> or word1, word2: ')
#print('\n\n')
#choice_word = "zao an"   # Test word
# create for loop to enter multiple words sep by ','
#lines = []
#lines.append(choice_word)
# remove ',' delimeter
#lines[0] = lines[0].rstrip(',')
# (1) Get the filename from user
#user_file = 'sample.txt'                       # Del line @ end of project
#user_file = 'sample2.txt'                      # del after project completion
# then get file and yada yada yada
# if ('.' is in choice_word):


# Function get_file()
# Description: Reads/imports the user defined file
# Calls:
# Parameters: string filename
# Returns: string lines

def get_file(filename):

    # Declare local variables
    infile = filename
    lines = []

    # Open the file
    infile = open(infile, 'r')

    # Read record description fields
    lines = infile.readlines()

    # Strip the ',' and '\n' from the description
    nLines = len(lines)
    for i in range(nLines):
        # Check if line has data
        #if (lines[i] == '\n'):
        lines[i] = lines[i].rstrip('\n')
        if (',' in lines[i]):
            lines[i] = lines[i].rstrip(',')
    # Else keep blank lines
    # End if

    #DEBUG(PRINT USER FILE) = PASS
    #for i in range(nLines):
        #print(lines[i])

    # Close the file
    infile.close()

    # Return values
    return lines

# End Function


'''
                   (2) PROCESS WORDS ONLINE

# (1) Request (get) webpage using word from user's file // response_obj
# (2) Check status of webpage
# (3) Transfer page into an parser object  // bs4_object
# (4) Parse and retireve data // string elements_2D_list
#       4.1) English-definition, Hanzi
'''

# Function process_lines()
# Description: Defines the words from lines[]
# Calls:
# Parameters: string terms[]
# Returns:

def process_lines(terms):

    # Declare local variables
    res     = []  # object Response
    soup    = []  # object Soup
    nTerms  = len(terms)  # len of term str
    nSoups  = 0   # length of Soup objects
    t_def   = []  # str Terms' definition
    t_hanzi = []  # str Terms' Hanzi
    t_roman = []  # str Terms' romanization

    # Request web pages
    for i in range(nTerms):
        # Init query for web address
        address = terms[i]
        address = address.replace(" ", "+")

        # Request the web page and store inside a response object
        #if (terms[i] != '\n'):
        response = requests.get('http://cantonese.org/search.php?q=' + address)
        # Else keep blank lines

        # Check status of web page
        # If web page loads successfully (prot: 200)
        #if (response.ok): # Else (prot: 400) = Don't create bs4 object
        response.raise_for_status()

        # Store response object inside a response list
        res.append(response)

        # Append a BeautifulSoup object in a bs4 list
        bs4_obj = (bs4.BeautifulSoup(res[i].text, "html.parser"))
        soup.append(bs4_obj)

    # End for


    # Loop through soup objects
    nSoups = len(soup)

    for i in range(nSoups):

        # Parse and store data
        t_roman.append(soup[i].select('.resulthead strong'))

        try:
            t_def.append(soup[i].select('.defnlist li')[0])

        except IndexError:
            try:
                t_def.append(soup[i].select('.resultbody')[0])

            except:
                t_def.append(' ')

        #definition.append(soup[i].select('.defnlist li'))
        t_hanzi.append(soup[i].select('.resulthead'))

    # End for

    # Return values
    return t_def, t_hanzi, t_roman

# End Function



'''
                   (3) OUTPUT TO FILE


# (1) Create a file for writing
# (2) Write the data as a record into the list: original word(s)
# (3) Write the data as a record into the list: parsed English-def, Hanzi
# (4) Close the file
'''

# Function write_file()
# Description: Writes parsed data to CSV outfile
# Calls:
# Parameters: str list lines,
#             str list t_def,
#             str list t_hanzi,
#             str list t_roman
# Returns: None

def write_file(lines, t_def, t_hanzi, t_roman):

    # Declare local variables
    not_def_num = []  # int line number from list
    not_defined = []  # str terms not defined
    s_def   = ''  # str term's definition
    s_hanzi = ''  # str term's hanzi
    s_roman = ''  # str term's romanization
    lenRows = len(t_roman)
    lenNotD = 0   # length of not_defined

    # Create files for writing
    outfile = open('canto-definitions.csv', 'w')
    #notFound_outfile = open('canto-not-defined.csv', 'w')

    # Init parsed text from bs4 objects
    for i in range(lenRows):
        try:
            s_roman = t_roman[i][0].getText()
            #print(t_roman[i][0])  # Displays obj if not found
        except:
            s_roman = lines[i]
        try:
            s_def = t_def[i].getText()
        except:
            print('NOT FOUND: LINE#', str(i+1), ': ', lines[i], sep='')
            s_def = t_def[i][0]

            # Append not_defined word list
            #not_def_num.append( str(i) )
            #not_defined.append( lines[0] )

    # Write the data to the outfile
        #print(s_roman, ', ', s_def, ', ', sep='', end='\n')
        outfile.write(s_roman + ',' + s_def + ',' + '\n')

    # End for

    # Display/Write to the not found outfile
    #lenNotD = len(not_defined)
    #for i in range (lenNotD):
        #print(not_defined)
        #notFound_outfile.write(not_def_num[i] + ',' + not_defined[i] + '\n')

    # (3) Close the file
    outfile.close()
    #notFound_outfile.close()



    # Display to Terminal
#        try:
#            s_roman = t_roman[i][0].getText()
#        except:
#            s_roman = lines[i]
#        try:
#            s_def = t_def[i].getText()
#        except:
#            s_def = ' '
#            print('NOT FOUND: Line#', str(i), ': ', lines[i], sep='')
#            notFound_file.write('Line #' +  str(i) + ',' + lines[i] + '\n')


# End Function

# Call the main function
main()
