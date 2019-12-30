#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Cantonese Dictionary
# Description:
#     Creates a Cantonese dictionary.
# Date: 2019/08/23
# Revised:
#     2019/09/07
#     2019/08/24

# list libraries used
import bs4, requests

def main():

    # Declare vars
    user_file = ''  # str filename
    lines   = []  # str lines from file
    t_def   = []  # str Terms' definition
    t_hanzi = []  # str Terms' Hanzi
    t_roman = []  # str Terms' romanization

    # Get user-defined file
    user_file = input('Enter the filename.ext: ')
    lines = get_file(user_file)

    # Process words online
    t_def, t_hanzi, t_roman = process_lines(lines)

    # Output to file
    write_file(lines, t_def, t_hanzi, t_roman)

# End Function

# Function get_file()
# Description: Reads/imports the user defined file
# Calls: None
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

    # Strip excessive characters
    nLines = len(lines)
    for i in range(nLines):
        # remove newline character
        lines[i] = lines[i].rstrip('\n')
        # remove commas
        if (',' in lines[i]):
            lines[i] = lines[i].rstrip(',')
        # End if
    # End for

    # Close the file
    infile.close()

    # Return values
    return lines

# End Function

# Function process_lines()
# Description: Defines the words from lines[]
# Calls: requests,
#        bs4;
# Parameters: string terms[]
# Returns:

def process_lines(terms):

    # Declare local variables
    res     = []  # object Response
    soup    = []  # object Soup
    nTerms  = len(terms)  # number of terms
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
        response = requests.get('http://cantonese.org/search.php?q=' + address)

        # Check status of web page
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

        # Append text from tags
        try:
            t_def.append(soup[i].select('.defnlist li')[0])
        except IndexError:
            try:
                t_def.append(soup[i].select('.resultbody')[0])
            except:
                t_def.append(' ')

        # Select hanzi from tags
        t_hanzi.append(soup[i].select('.resulthead'))

    # End for

    # Return values
    return t_def, t_hanzi, t_roman

# End Function

# Function write_file()
# Description: Writes parsed data to CSV outfile
# Calls: None
# Parameters: str list lines,
#             str list t_def,
#             str list t_hanzi,
#             str list t_roman;
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

    # Init parsed text from bs4 objects
    for i in range(lenRows):
        try:
            s_roman = t_roman[i][0].getText()
        except:
            s_roman = lines[i]
        try:
            s_def = t_def[i].getText()
        except:
            print('NOT FOUND: LINE#', str(i+1), ': ', lines[i], sep='')
            s_def = t_def[i][0]
        # Doesn't display Chinese correctly
        #s_hanzi = t_hanzi[i][0].getText()

        # Write the data to the outfile
        outfile.write(s_roman + ',' + s_def + ',' + '\n')

    # End for

    # Close the file
    outfile.close()

# End Function

# Call the main function
main()

