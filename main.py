# Step 0 : install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"

# Step 1 : get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)   #to show the soup content in pretty form

# Step 3 : HTML Tree traversal 
    # get the title of html page
title = soup.title
    # print(title)

    # get all the paragraph from the page
paras = soup.find_all('p')
    # print(paras)

    # to get the first para/element of the html page
print(soup.find('p'))

    # to get classes of any element of the html page
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p", class_ ="lead"))

# get the text from the tags/soup
print(soup.find('p').get_text())


# get all the anchor from the page
anchors = soup.find_all('a')
all_links = set()
# get all the links on the page

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.codewithharry.com/" +link.get('href')
        all_links.add(link)        # here, set will give only single link in case same link is used multiple times on page
        print(linkText)


