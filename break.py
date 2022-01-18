
import random as rd
import csv

# list_of_folks = ["Jerry", "Nuhu", "Ahmed", "Tobi", "George", "Teco"]
# while len(list_of_folks) > 1:
#     list_of_folk = rd.choice(list_of_folks)
#     list_of_folks = [x for x in list_of_folks if x not in list_of_folk]
#     print(list_of_folks) 

info = []
info.append([sneaker_brand,sneaker_description,sneakers_old_price,new_price_range_one,new_price_range_two,sneakerd_new_price,d_discount,sneaker_rating])

            

def zas():
    
    names = input("Register name here: ")
    # print(nam
    return names


def write(names):
    zas()
    write_it = open("C:/users/denra/Documents/univiel city class/broken.csv", mode="a",encoding= "utf-8", newline="")
    pen =csv.writer(write_it)
    write_it.write(names)


    def read_it():
    
        names=zas()
        write("gg")
        write_it = open("C:/users/denra/Documents/univiel city class/broken.csv", mode= "r")
        Read_file = write_it.readlines()
        for x in Read_file:
            if names == x:
                print("Tobi")
        read_it()