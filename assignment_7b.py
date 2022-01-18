import csv

import requests
from bs4 import BeautifulSoup as BS
from csv import writer




url = "https://jumia.com.ng/men-sneakers/"
headers = requests.utils.default_headers()
headers.update({
   "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
})

with open("jumiaSneakers.csv", "w",encoding= "utf-8",newline= "") as f:
   thewriter = writer(f)
   header = ["sneakers Brand", "sneakers Description", "sneakers old Price", "sneakers new price lower","sneakers newprice upper", "New price","Discount","Phone Rating"]
   thewriter.writerow(header)
   for x in range (1,51):
        my_response = requests.get(f"https://www.jumia.com.ng/men-sneakers/?page={x}#catalog-listing")
        # print(my_response.status_code)
        first_soup = BS(my_response.content, features = "lxml")
        soup2 = first_soup.find("div", attrs={"class":"-paxs row _no-g _4cl-3cm-shs"})
        # print(soup2)

        list_soups = soup2.find_all("article", attrs = {"class":"prd _fb col c-prd"})

        for soup in list_soups:
            # print(soup.prettify())
            sneaker_details = soup.find ("a")
            try:
                sneaker_brand = sneaker_details.get("data-brand")
                # print(sneaker_brand)    
            except:     
                sneaker_brand = None
            try:
                sneaker_description = sneaker_details.get("data-name")
                #   print(sneaker_description)
            
            except:
                sneaker_description = None

            try:
                old_div = soup.find("div", attrs = {"class" : "old"})
                sneakers_old_price = int((old_div.text).lstrip("₦").replace(",", ""))
                # print(sneakers_old_price)
            except:
                sneakers_old_price = None

            try: 
                new_div = soup.find("div", attrs = {"class" : "prc"}).text
                if " - " in new_div: 
                        pass
                else:
                    sneakers_new_price = int((new_div).lstrip("₦ ").replace(",", ""))
                       
                sneakers_low_range_price = soup.find("div", attrs = {"class" : "prc"}).text
                if " - " in sneakers_low_range_price:
                        n = (sneakers_low_range_price).split(" - ")[0]
                        n = int(sneakers_low_range_price.lstrip("₦ ").replace(",", ""))
                        # print(low_range_price)
                else:
                    pass
            
                sneakers_high_range_price = soup.find("div", attrs = {"class" : "prc"}).text
                if " - " in sneakers_high_range_price:
                        ne = (sneakers_high_range_price).split(" - ")[1]
                        ne = int(ne.lstrip("₦ ").replace(",", ""))
                        

                
                    
        
                    
                    
                
                

            except:
                n = None
                ne = None
                sneakerd_new_price = None

            try:
                d_discount = soup.find("div",class_= "tag _dsct _sm").text
                        
                # print(d_discount)
            except:
                d_discount = None
                
            try:
                rating = soup.find("div", attrs = {"class" : "stars _s"})
                sneaker_rating = float((rating.text).replace(" out of 5", ""))
                # print(sneaker_rating)

            except:
                sneaker_rating = None 

            info = [sneaker_brand ,  sneaker_description,  sneakers_old_price,n,ne,sneakerd_new_price,  d_discount, sneaker_rating]
            thewriter.writerow(info)
     
        
                
                

            

        
        
    

