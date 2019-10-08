#This File was made by Krishna Pandian 
#Organization Affiliation: CruzHacks


#This is a Sample File for Reference
#In This Code Sample We will Show the important aspects of web scraping




'''
What is Web Scraping?

Web Scraping is the extraction of Data from Web Sites.
Data can be Saved on databases or in any spreadsheet format.


Tips:
* Try websites without dynamic JS
* If there is an API that allows to normally get the data, pull it normally



Important Notes about Web Scraping:
    
* Web Scraping is Not Scalable and thus will not work on all websites    
* Web Scraping can lead to legal issues with Data ownership
* Having and Understanding of how HTML and CSS work will help with the process



For this demonstration we will be using the Beautiful Soup Library
Official Documentation can be found @ https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html

'''

#This function below will show you how you can parse Websites
#For this Example I will be showing how we can parse information of the New York Times


from bs4 import BeautifulSoup #Library that allows for Web Scraping
                              #Built into Most IDEs and working environments

#These are the other libraries I will be using today
import requests
from datetime import date


website = "https://www.nytimes.com"


def get_date(): #This function is only used so users can retrieve the recent dates
    today_parsed = date.today()
    today = today_parsed.strftime("%Y/%m/%d")   
    return today

    
def parse_articles():   #This function is the Most Important Function with Beautiful Soup
    today = get_date()
    result = requests.get(website)  
    src = result.content
    soup = BeautifulSoup(src, "lxml")       
    links = soup.find_all('a', href = True)
    
    
    head_tag = soup.head
    head_tag.contents
    title_tag = head_tag.contents[0]
    
    
    list_of_links = []
    for link in links:
        if today in link['href']:                        #allows to look for a type scraped
            list_of_links.append(website + link['href']) #store the links in a list
            print(list_of_links)     
'''
Do not recommend using this method but you can download html files and parse it through their


def use_html_files():
    with open("") as fp:
    soup = BeautifulSoup(fp)                   
'''        
            
'''
Ways to make your project cool
* Use data analytics like Jupter notebook to make regression predictions
* Scrape the data and redistribute it LEGALLY
* Put the data into a web application
'''
    



    
  


