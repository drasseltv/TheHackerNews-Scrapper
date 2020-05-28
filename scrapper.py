from pathlib import Path  # python3 only
from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
from bs4 import BeautifulSoup
import requests
import ssl
import os


def save_in_mongo(doc):
    """
    Saves the document into mongoDB
    """
    try:
        collection.insert_one(doc)
        print("Data Added")
    except:
        print("An error occured")


def get_article_body(url):
    """
    gets into a particular blog and steals the ARTICLE BODY away :P
    """
    data = requests.get(url)
    soupx = BeautifulSoup(data.text, 'html.parser')
    body = ""
    for data in soupx.find_all('div', {'class': 'articlebody'}):
        body += data.text.strip()
    return body


def extract_n_collect(url):
    """
    Extracts data from thehackernews.com and combines them into a JSON(dict).
    """
    data = requests.get(url)
    soupx = BeautifulSoup(data.text, 'html.parser')
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
    
    next_url = soupx.find('a', {'class':'blog-pager-older-link-mobile'})['href']
    
    for i in range(0, len(titles)):
        if links[i] in avoid_links:
            continue
            
        body = get_article_body(links[i])

        avoid_links.add(links[i])
        
        doc = {'_id': links[i], 'title': titles[i], 'meta': {
            'author': authors[i], 'published': published[i], 'description': descriptions[i],'article_body' : body}}
            
        save_in_mongo(doc)
        
    return next_url

if __name__ == '__main__':
    
    USERNAME = "admin"
    PASSWORD = "top_secret"
    
    try:
        my_cluster = MongoClient(
            "mongodb+srv://"+USERNAME+":"+PASSWORD+"@scrapx-oib7y.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
    except pymongo.errors.ConnectionFailure as e:
        print("MongoDB couldnt be connected  \n" + e)

    titles = []
    links = []
    img_urls = []
    descriptions = []
    published = []
    authors = []



    db = my_cluster["scrapDB"]
    collection = db["thehackernews"]
    url = "https://thehackernews.com/"
    avoid_links = set()
    for _ in range(500):
        url = extract_n_collect(url)
        #print(url)
    
