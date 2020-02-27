Cantonese Dictionary
####################
:Author: David Boyd
:Date: Fall 2019
:Type: Web Scraper

Description
===========

This web scraper program translates Cantonese words to English words.

How it Works
============

Input
-----

The program begins by reading in a text file that contains a wordlist to be
translated or defined.

Process
-------

The program then runs these terms into **cantonese.org** to scrap the first
definition and jyutping (if available).

#.	Create a query web address from a word in the wordlist.
#.	*Requests* library uses the (HTTP) GET method to download the corresponding reponse webpage.
#.	Move the response into *BeautifulSoup4* (HTML parser) object.
#.	Extract specific data based on the HTML tags and index.

Output
------

The program creates a file called "canto-definitions.csv" in which the first
column displays the jyutping and the second column displays the definition.

That's it!
----------

You can view your new "canto-dict.csv" from the current working directory.

How to Run Program
==================

Dependencies
------------

	- BeautifulSoup4  (HTML parser)
	- Requests (HTTP library)

Run
---

.. code-block :: Bash

	# Run program
	python3 main.py

	# Input wordlist
	sample/sample2.txt

	# Review the saved file
	vim canto-definitions.csv


