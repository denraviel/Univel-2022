for x in range(1,50):

      my_response = requests.get(f"https://www.jumia.com.ng/smartphones/?page={x}#catalog-listing")
      print(my_response.status_code)

      first_soup = BS(my_response.content, features = "lxml")
      second_soup = first_soup.find("div", attrs= {"class" : "-paxs row _no-g _4cl-3cm-shs"})
      # print(second_soup)

      list_of_soups =  second_soup.find_all("article", attrs = {"class": "prd _fb col c-prd"})