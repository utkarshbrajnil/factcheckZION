import requests, webbrowser
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request

user_input = input("enter somethiong to search: ")
print("searching for the fact....")

google_search = requests.get("https://www.google.com/search?q="+user_input+"factcheck")

#print(google_search.text)

soup = BeautifulSoup(google_search.text, 'html.parser')
#print(soup.prettify())

search_results = soup.select('.kCrYT a')
#print(search_results)
results=[]

for link in search_results[:5]:
    actual_link=link.get('href')
    print(actual_link)
    link_result=urllib.request.urlopen("https://google.com" +actual_link).read()
    soup=BeautifulSoup(link_result, 'lxml')
    #print(soup)
    nav=soup.nav
    body=soup.body
    for paragraph in body.find_all('p'):
        results.append(paragraph.text)
  #  for div in soup.find_all('div'):
  #      print(div.text)

for r in results:
    print(r)
    print("\n")

#print(len(results))



'''in the above code all the webpage links are stored in the list search_results
in order of their appearance in the result of google search. By using the for loop
we are selecting the top 5 links and printing the link'''

    
  
    
