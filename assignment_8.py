import requests
from bs4 import BeautifulSoup as BS



url = "https://punchng.com/?s=banditry+and+kidnapping"
headers = requests.utils.default_headers()
headers.update({
   "user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})

my_response = requests.get(url, headers)
# print(my_response.status_code)
first_soup = BS(my_response.content, features = "lxml")
second_soup = first_soup.find("div", attrs= {"class" : "entries-grid row"})
# print(second_soup)
list_of_soup = second_soup.find_all("div", attrs={"class" : "grid-item"})
for soup in list_of_soup:
   # print(soup.prettify())
   linu = soup.find("a").attrs["href"]
   print(linu)
   try:
      linu2 = str(linu.get("href"))

      
   except:
      None
   
   
