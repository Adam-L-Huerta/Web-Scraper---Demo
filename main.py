from bs4 import BeautifulSoup
import requests


search = input("Search for: ")
params = {"q": search}

r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_href and item_text:
        print(item_text)
        print(item_href)

       # print("Summary: ", item.find("a").parent.parent.find("p").text)

        children = item.children
        for child in children:
            print("Child", child)




'''
from bs4 import BeautifulSoup
import requests

Learning to "Web Scrape"

search = input("Enter search term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text)
print(soup.prettify())
'''