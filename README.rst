Cantonese Dictionary
####################
:Author: David Boyd
:Date: FALL 2019

Description
===========

This web scraper program defines Cantonese/English words into jyutping with its English definitions!

How it Works
============

Input
*****
This program reads in a text file that contains a list of words.

Process
*******
The program then runs these terms into Cantonese.org and scrapes the first
definition and jyutping (if available).

Output
******
The program creates a file called "canto-definitions.csv" in which the first
column displays the jyutping and the second column displays the definition.

How to Run Program
==================

1. Install:

	- pip  (Python's Package Manager)
	- BeautifulSoup4  (Web Scraper)
	- requests (HTTP library)

2. Run:

	- Enter the text file you wish to process with its extension.  I.e.) sample.txt

3. That's it!

	- You can view your new "cantonese-dict.csv" from the same directory as this program.
