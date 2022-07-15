# UglySoup

UglySoup is a script that allows users to download different file types from a website. The user will provide a URL and a filetype and the script will query the HTML of that URL and download any files of the specified file type, if any.

Example: download all pdfs from website

$ python uglysoup.py <br/>
  &nbsp;&nbsp; -url https://bulletproofscreenwriting.tv/breaking-bad-tv-script-download/ <br/>
  &nbsp;&nbsp; -filetype pdf

# Requirements

&nbsp;&nbsp; $ sudo apt-get install python3.6

&nbsp;&nbsp; $ python3 get-pip.py

&nbsp;&nbsp; $ pip3 install beautifulsoup4

# Run 

From the terminal, run:

$ python uglysoup.py <br/>
  &nbsp;&nbsp; -url "https://www.hello.com" <br/>
  &nbsp;&nbsp; -filetype "png" <br/>
  &nbsp;&nbsp; -filename "hellopng" <br/>
  &nbsp;&nbsp; -location "/Users/you/Desktop"
