import os
from bs4 import BeautifulSoup
from datetime import datetime
import argparse
from urllib.request import Request, urlopen

# creating a file and writing it into a string 
def download(outdir, filename, link, format):
    file = open(outdir + filename + format, 'wb') 
    file.write(urlopen(link).read()) 
    file.close() 

# argparse to gather various info from user
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", type=str, required = True)
    parser.add_argument("-filetype", type=str, required = True)
    parser.add_argument("-filename", type=str, required = True)
    parser.add_argument("-location", default = "./" , type=str, required= False)
    args = parser.parse_args()

    return args

# creates a path to store downloaded files
def create_path(args):
    
    if not args.location.endswith("/"):
        args.location = args.location + "/"
    if not os.path.exists(args.location):
        print("path", path, "doesn't exist")
        return
    path = args.location + "uglysoup/"
    if not os.path.exists(path):
        os.makedirs(path)
    path = path + args.filetype + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    ts = datetime. now(). strftime("%Y_%m_%d-%I:%M:%S_%p")
    path = path + ts + "/"
    if not os.path.exists(path):
        os.makedirs(path)

    return path

#beautiful soup function to parse through html
def main():
    args = arg_parse()
    path = create_path(args)

    response = Request(args.url, headers = {'User-Agent': 'Mozilla/5.0'})
    html = urlopen(response).read()
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    for link in soup.find_all('a'):
        if link['href'].endswith(args.filetype):
            print(link["href"])
            try:
                download(path, args.filename + str(counter), link["href"], "." + args.filetype)
            except:
                print("invalid url")
            counter += 1

# calls main function to run code
if __name__ == "__main__":
    main()