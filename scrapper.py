from pathlib import Path  # python3 only
from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
from bs4 import BeautifulSoup
import requests
import ssl
import os

USERNAME = "admin"
PASSWORD = "top_secret"

data = requests.get("https://thehackernews.com/")
soupx = BeautifulSoup(data.text, 'html.parser')

titles = []
links = []
img_urls = []
descriptions = []
published = []
authors = []


try:
    my_cluster = MongoClient(
        "mongodb+srv://"+USERNAME+":"+PASSWORD+"@scrapx-oib7y.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
except pymongo.errors.ConnectionFailure as e:
    print("MongoDB couldnt be connected  \n" + e)

db = my_cluster["scrapDB"]
collection = db["thehackernews"]


for title in soupx.find_all('h2', {'class': 'home-title'}):
    titles.append(title.text)

for link in soupx.find_all('a', {'class': 'story-link'}):
    links.append(link['href'])

for img_url in soupx.find_all('img', {'class': 'home-img-src'}):
    img_urls.append(img_url['data-src'])

for desc in soupx.find_all('div', {'class': 'home-desc'}):
    descriptions.append(desc.text.strip())

for info in soupx.find_all('div', {'class': 'item-label'}):
    published.append(info.text[1:info.text.find('202')+4])
    authors.append(info.text[info.text.find('202')+5:].strip())

for i in range(0, len(titles)):
    doc = {'_id': links[i], 'title': titles[i], 'meta': {
        'author': authors[i], 'published': published[i], 'description': descriptions[i]}}
    try:
        collection.insert_one(doc)
        print("Data Added")
    except:
        print("An error occured")
