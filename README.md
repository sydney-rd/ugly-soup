# UglySoup

One of my favorite projects, Ugly Soup allows you to seamlessly download files from any URL of your choosing.

Enter a URL, pick a filetype, filename, and a location for the files to be stored, and using BeautifulSoup, the filetype will be extracted from the URL and saved to the location chosen. You can also run -h for help.

# Install BeautifulSoup

python3 get-pip.py

pip3 install beautifulsoup4

# Run uglysoup.py

From the terminal, run:

$ python uglysoup.py -url -filetype -filename -location (optional)

### Example of what to run:

$ python uglysoup.py -url https://www.scriptslug.com/script/breaking-bad-101-pilot-2008 -filetype pdf -filename breakingbad -location
/Users/sydneydavid/Github/UglySoup

Uses argparse to gather info.

- Add a URL after -url
- Add a filetype after -filetype (any filetype within an 'a' tag and 'href' i.e. pdf, png, jpg)
- Add any filename
- Add a -location for files to be downloaded and saved. Location is optional as its default is the directory you are working out of.
