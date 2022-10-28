#!/usr/bin/python3
import re, urllib
import pandas as pd
from bs4 import BeautifulSoup
import sys 

query = "+" + sys.argv[1] + " ungdom" + " kokain" + " narkotika" + " hasj"
#hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
hdr =  { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30' }
urlquery = urllib.parse.quote_plus(query)
print (urlquery)
req = urllib.request.Request("http://duckduckgo.com/html/?q=" + urlquery + "&kl=no-no", headers=hdr)
site = urllib.request.urlopen(req)
data = site.read()
soup = BeautifulSoup(data, "html.parser")

my_list = soup.find("div", {"id": "links"}).find_all("div", {'class': re.compile('.*web-result*.')})[0:10]

(result__snippet, result_url) = ([] for i in range(2))

for i in my_list:         
    try:
        result__snippet.append(i.find("a", {"class": "result__snippet"}).get_text().strip("\n").strip())
    except:
        result__snippet.append(None)
    try:
        result_url.append(i.find("a", {"class": "result__url"}).get_text().strip("\n").strip())
    except:
        result_url.append(None)


for item in result_url:
    print (item)
