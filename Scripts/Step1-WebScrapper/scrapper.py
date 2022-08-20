import requests
import pandas as pd
import numpy as np
from tqdm import tqdm
from bs4 import BeautifulSoup
from requests.exceptions import Timeout

html = requests.get("https://www.ccarprice.com/au/") #This is the website this script uses to scrape needed information
soup = BeautifulSoup(html.content, 'html.parser') #Turning response object fom "html" variable into beautifulsoup object to crawl through the site

mydivs = soup.find("div", {"class": "vertical-menu"}).label.find("div", {"class": "show1"}).find_all("a", {"class": "brnd"})
links = [x.get("href") for x in mydivs] #This list will store links of all car brands given in the website

df = pd.DataFrame() #Empty pandas dataframe which will be filled later

for link in tqdm(links, desc="          TOTAL: "): #tqdm ------> Progress bar in python
    # Here each 'link' element above is an actual link to webpage containing cars of a single car brand
    html1 = requests.get(link)
    soup1 = BeautifulSoup(html1.content, 'html.parser')

    all_cars_of_this_brand = soup1.body.find("div", {"id": "page"}).find_all("div", {"id": "pbox", "class": "price-cover"})[-1].find_all("div", {"id": "pbox", "class": "listing"})

    all_cars_links_of_this_brand = [] #This list will store the links of all car correponding to a current car brand

    for i in all_cars_of_this_brand: #Extracting just the links of each needed cars
        text = i.getText().strip()
        if text.split("\n")[-1] != "Coming soon":
            all_cars_links_of_this_brand.append(i.a.get("href"))

    
    for i in tqdm(all_cars_links_of_this_brand, desc="RETRIEVING DATA: ", leave=False): #Looping over links of each car of the current car brand to extract useful informations
        try:
            html2 = requests.get(i, timeout=10) #setting a timeout for server response
        except Timeout:
            continue #continuing to next webpage if timeout exceeds
        else: #If timeout doesn't exceed, extracting data
            soup2 = BeautifulSoup(html2.content, 'html.parser')

            car = soup2.body.find("div", {"id": "page", "class": "main"}).div.h1.span.find_all("span")
            brand, _ = [x.getText() for x in car] ########

            price_aud = soup2.body.find("div", {"id": "page", "class": "main"}).div.find("div", {"id": "pbox", "class": "detail-cover"}).getText().strip().split("\n")[0].split(" ")[-1]
            
            table = soup2.body.find("div", {"id": "page", "class": "main"}).div.find("div", {"id": "spec"}).div.find_all("div", {"class": "tr"})
            

            if link == links[0] and i == all_cars_links_of_this_brand[0]:
                dict_for_df = {"price in aud": price_aud, "brand": brand}
                for j in table:
                    obj =  j.getText().strip().lower().split("\n")
                    obj = [x.strip() for x in obj]
                    title, value = obj[0], obj[1]
                    dict_for_df[title] = value
                df = pd.DataFrame(dict_for_df, index=[0])
            else:
                dict_for_df = {"price in aud": price_aud, "brand": brand}
                not_existing_columns = {}
                for j in table:
                    obj =  j.getText().strip().lower().split("\n")
                    obj = [x.strip() for x in obj]
                    title, value = obj[0], obj[1]
                    if title in df.columns:
                        dict_for_df[title] = value
                    else:
                        not_existing_columns[title] = value
                
                if len(not_existing_columns) != 0:
                    df.loc[len(df.index)] = dict_for_df

                    for i in list(not_existing_columns.keys()):
                        before_below = [np.nan for d in range(1,len(df.index))]
                        before_below.append(not_existing_columns[i])
                        not_existing_columns[i] = before_below

                    df1 = pd.DataFrame(not_existing_columns)
                    df =  pd.concat([df, df1], axis = 1)
                    
                else:
                    df.loc[len(df.index)] = dict_for_df
            df.to_csv('temp/temp.csv', index=False) #saving each time script scrapes from a webpage

df.to_csv('car_prices_australia.csv', index=False) #Finally saving the complete file