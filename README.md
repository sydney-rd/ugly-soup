# UglySoup

Enter a URL, pick a filetype, filename, and a location for the files to be stored, and using Beautiful Soup, the filetype will be extracted from the URL and saved to the location chosen

# Requirements

$ sudo apt-get install python3.6

python3 get-pip.py

pip3 install beautifulsoup4

# Run 

From the terminal, run:

$ python uglysoup.py -url -filetype -filename -location 

Example:

$ python uglysoup.py -url https://bulletproofscreenwriting.tv/breaking-bad-tv-script-download/ -filetype pdf -filename breakingbad -location 
/Users/sydneydavid/Github/UglySoup

Description:

Uses argparse to gather info. Add a URL after -url, a filetype after -filetype (any filetype within an 'a' tag and 'href' i.e. pdf, png, jpg) -filename and -location for files to be downloaded and saved. Location is optional as its default is the directory you are working out of. 

