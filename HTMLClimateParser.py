#!/usr/bin/env python
# coding: utf-8

# In[14]:


import urllib.request 
from pprint import pprint
from html_table_parser import HTMLTableParser
import pandas as pd
headers={'User-Agent':'Whatever'}
def url_get_contents(url):
    req= urllib.request.Request(url=url,headers=headers)
    f=urllib.request.urlopen(req)
    return f.read()


# In[15]:


xhtml=url_get_contents('https://en.climate-data.org/asia/india/hyderabad/hyderabad-2801/').decode('utf-8')
p=HTMLTableParser()
p.feed(xhtml)
pprint(p.tables[1])
print("\n\nPANDAS DATAFRAME\n") 
print(pd.DataFrame(p.tables[3]))

