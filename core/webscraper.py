import requests, webbrowser
from bs4 import BeautifulSoup

user_input = input("enter somethiong to search: ")
print("searching for the fact....")

google_search = requests.get("https://www.google.com/search?q="+user_input+"factcheck")

#print(google_search.text)

soup = BeautifulSoup(google_search.text, 'html.parser')
#print(soup.prettify())

search_results = soup.select('.kCrYT a')
#print(search_results)

for link in search_results[:5]:
    print(link.get('href'))

'''in the above code all the webpage links are stored in the list search_results
in order of their appearance in the result of google search. By using the for loop
we are selecting the top 5 links and printing the link'''

    
  
    
