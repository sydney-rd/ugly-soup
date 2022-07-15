# UglySoup

UglySoup is a script that allows users to download different file types from a website. The user will provide a URL and a filetype and the script will query the HTML of that URL and download any files of the specified file type, if any.

Example: download all pdfs from website

$ python uglysoup.py &nbsp;&nbsp;
  -url https://bulletproofscreenwriting.tv/breaking-bad-tv-script-download/ &nbsp;&nbsp;
  -filetype pdf

# Requirements

$ sudo apt-get install python3.6

python3 get-pip.py

pip3 install beautifulsoup4

# Run 

From the terminal, run:

$ python uglysoup.py 
  -url "https://www.hello.com" 
  -filetype "png" 
  -filename "hellopng" 
  -location "/Users/you/Desktop"
