import requests
from bs4 import BeautifulSoup as BS
from csv import writer



url = "https://.jumia.com.ng/smartphones/"
headers = requests.utils.default_headers()
headers.update({
   "user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
})
with open("jumiaSmartphone.csv", "w",encoding= "utf-8",newline= "") as f:
   thewriter = writer(f)
   header = ["Phone Brand", "Phone Description", "Old Price", "New price","Discount","Phone Rating"]
   thewriter.writerow(header)


   for x in range(1,51):

      my_response = requests.get(f"https://www.jumia.com.ng/smartphones/?page={x}#catalog-listing")
      print(my_response.status_code)

      first_soup = BS(my_response.content, features = "lxml")
      second_soup = first_soup.find("div", attrs= {"class" : "-paxs row _no-g _4cl-3cm-shs"})
      # print(second_soup)

      list_of_soups =  second_soup.find_all("article", attrs = {"class": "prd _fb col c-prd"})

      for soup in list_of_soups:
         # print(soup.prettify())
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
            phone_description = "no description"

         #for old prize
         try:
            old_div = soup.find("div", attrs = {"class" : "old"})
            phone_old_price = int((old_div.text).lstrip("₦").replace(",", ""))
            # print(phone_old_price)
            
         except:
            phone_old_price = "nil"

         #for new prize
         try: 
            new_div = soup.find("div", attrs = {"class" : "prc"})
            phone_new_price = int((new_div.text).lstrip("₦").replace(",", ""))
            # print(phone_new_price)

         except:
            phone_new_price = None
      #for discount
         try:
            dis_discount = soup.find("div",class_= "tag _dsct _sm").text
            
            print(dis_discount)

         except:
            dis_discount = "no discount"

         #for phone rating
         try:
            rating = soup.find("div", attrs = {"class" : "stars _s"})
            phone_rating = float((rating.text).replace(" out of 5", ""))
            # print(phone_rating)

         except:
            phone_rating = "no rating"

         

         info = [phone_brand,  phone_description,  phone_old_price,  phone_new_price,  dis_discount,  phone_rating]
         thewriter.writerow(info)
         






         



      
         