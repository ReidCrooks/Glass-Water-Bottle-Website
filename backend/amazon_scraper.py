from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random
import sqlite3

def get_title(soup):
    
    try:
        title = soup.find("span", attrs={"id":"productTitle"})
        title_value = title.text
        title_string = title_value.strip()
        
    except AttributeError:
        title_string = ""

    return title_string
    
def get_price(soup):
    
    try:
        price = soup.find("span", attrs={"class":"a-price aok-align-center"}).find("span", attrs={"class":"a-offscreen"})
        price_text = price.text
        
    except AttributeError:
        price_text = ""
    
    return price_text

def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

def get_reviews(soup) :
    try:
        reviews = soup.find('span', attrs={'id':'acrCustomerReviewText'}).text.strip()
    except AttributeError:
        reviews = ""
        
    return reviews

def get_size(soup):
    try:
        size = size = soup.find('span', attrs={'class':'a-size-base a-color-base inline-twister-dim-title-value a-text-bold'}).text.strip()
    except AttributeError:
        size = ""
    
    return size



URL = "https://www.amazon.com/s?k=glass+water+bottles&crid=2DT9YU6JDUFY&sprefix=glass+water+b%2Caps%2C534&ref=nb_sb_noss_2"

USER_AGENTS = [
    # Chrome (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",

    # Chrome (macOS)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36",

    # Chrome (Linux)
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",

    # Firefox (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",

    # Firefox (macOS)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0",

    # Edge (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",

    # Safari (macOS)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",

    # Opera (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.172",

    # iPhone Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",

    # iPad Safari
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",

    # Android Chrome
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",

    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",

    # Samsung Internet
    "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G973U) AppleWebKit/537.36 "
    "(KHTML, like Gecko) SamsungBrowser/14.0 Chrome/91.0.4472.164 Mobile Safari/537.36",

    # Internet Explorer 11
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

    # UC Browser (Android)
    "Mozilla/5.0 (Linux; U; Android 9; en-US; Redmi Note 7 Pro) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 UCBrowser/12.13.2.1005",

    # Brave (Desktop)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",

    # Vivaldi (Desktop)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Vivaldi/4.1",

    # QQ Browser (China)
    "Mozilla/5.0 (Linux; U; Android 10; zh-cn; VOG-AL10 Build/HUAWEIVOG-AL10) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 MQQBrowser/11.2 Mobile Safari/537.36",

    # Yandex Browser
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/89.0.4389.82 YaBrowser/21.3.3.183 Yowser/2.5 Safari/537.36",

    # Amazon Silk (Kindle)
    "Mozilla/5.0 (Linux; U; Android 9; en-US; KFMAWI Build/PS7276.180610.315) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Silk/80.2.2 like Chrome/80.0.3987.132 Safari/537.36"
]

# Randomly select a User-Agent
HEADERS = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'DNT': '1'  # Do Not Track
}

webpage = requests.get(URL, headers=HEADERS)

# convert webpage content to html
soup = BeautifulSoup(webpage.content, "html.parser")

links = soup.find_all("a", attrs={"a-link-normal s-line-clamp-4 s-link-style a-text-normal"})
links_list = []

# put all links in a list
for link in links:
    links_list.append(link.get('href'))
    
d = {"title":[], "price":[], "rating":[], "reviews":[],"size":[]}
# Loop for extracting product details from each link 
for link in links_list:
    new_webpage = requests.get("https://amazon.com" + link, headers=HEADERS)
    new_soup = BeautifulSoup(new_webpage.content, "html.parser")
    
    # Function calls to display all necessary product information
    d['title'].append(get_title(new_soup))
    d['price'].append(get_price(new_soup))
    d['rating'].append(get_rating(new_soup))
    d['reviews'].append(get_reviews(new_soup))
    d['size'].append(get_size(new_soup))


amazon_df = pd.DataFrame.from_dict(d)
amazon_df['title'] = amazon_df['title'].replace('', np.nan)
amazon_df = amazon_df.dropna(subset=['title'])
amazon_df.to_csv("amazon_data.csv", header=True, index=False) 

conn = sqlite3.connect("amazon_products.db")
amazon_df.to_sql("products", conn, if_exists="replace", index=False)
conn.close()