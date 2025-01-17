from bs4 import BeautifulSoup
import requests


search = input('Enter search term: ')
param = {"q":search}
r = requests.get("http://bing.com/search",params = param)

soup = BeautifulSoup(r.text,"html.parser")
results = soup.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print (item_text)
        print (item_href)
        print('Summary:', item.find("a").parent.parent.find("p").text)

        children = item.find("h2")
        print('Next sibling of h2 is:', children.next_sibling)
