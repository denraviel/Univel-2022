import requests
from bs4 import BeautifulSoup as BS



url = "https://jumia.com.ng/smartphones/"
headers = requests.utils.default_headers()
headers.update({
   "user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})

my_response = requests.get(url, headers)
print(my_response.status_code)

first_soup = BS(my_response.content, features = "lxml")
second_soup = first_soup.find("div", attrs= {"class" : "-paxs row _no-g _4cl-3cm-shs"})
# print(second_soup)

list_of_soups =  second_soup.find_all("article", attrs = {"class": "prd _fb col c-prd"})

for soup in list_of_soups:
   print(soup.prettify())
   phone_details = soup.find ("a")
   ##for phone brand
   try:
      phone_brand = phone_details.get("data-brand")
      # print(phone_brand)
   
   except:
      phone_brand = None
#for phone spec
   try:
      phone_description = phone_details.get("data-name")
      # print(phone_description)

   except:
      phone_description = None
#for old prize
   try:
      old_div = soup.find("div", attrs = {"class" : "old"})
      phone_old_price = int((old_div.text).lstrip("₦").replace(",", ""))
      # print(phone_old_price)
      # a = phone_old_price.lstrip("₦")
      # d = a.split(",")
      # string = [str(integer) for integer in d]
      # a_sring = "".join(string)
      # an_integer = int(a_sring)
      # print(an_integer)
   except:
      phone_old_price = None
#for new prize
   try: 
      new_div = soup.find("div", attrs = {"class" : "prc"})
      phone_new_price = int((new_div.text).lstrip("₦").replace(",", ""))
      # print(phone_new_price)

   except:
      phone_new_price = None
#for discount
   try:
      dis_discount = soup.find("div", attrs = {"class" : "tag _dsct _sm"})
      dist_discount = dis_discount.text
      print(dist_discount)

   except:
      dist_discount = None

   #for phone rating
   try:
      rating = soup.find("div", attrs = {"class" : "stars _s"})
      phone_rating = float((rating.text).replace(" out of 5", ""))
      # print(phone_rating)

   except:
      phone_rating = None

   break


