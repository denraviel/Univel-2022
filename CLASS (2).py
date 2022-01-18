#TASK 1
# task = input("")
# print(task)

# tee = task.split(" ")
# print(tee)

# tes = int(tee[0])
# tes1 = int(tee[1])

# ave = (tes + tes1)/ 2
# print(ave)

# # LEN
# scores = [30, 50, 43, 5]
# # number = len(scores)
# # print(number)

# ZIP
# bee = ("ex", "lin", "out")
# bed = (1, 2, 3,)
# output = zip(bee, bed) 
# put = list(output)
# print(put)

# ENUMERATE
# SAY = ["face", "eyes", "leg"]
# out = enumerate(SAY)
# print(list(out))

# LAMBDA
# add = lambda x: x + 100
# print(add(2))
# OR 
#aid = add(2)
#print(aid)
#---------------------------------------------------------------------------------
#checker = lambda a : a.startswith(is)
#output = checker(This is just a string)
#print(output)

#MAP
# up_score = map(lambda a : a + 2, scores)
# output = list(up_score)
# print(output)
# #------------------------------------------------------------------------------------------
# list_of_names = ["steve", "dwayne", "freya", "nelson"]
# nam = map(lambda a : a.title(), list_of_names)
# jam = list(nam)
# print(jam)

# num = [10, 20, 31, 45, 60, 77]
# my_filter = filter(lambda a : a % 2, num)
# jam = list(my_filter)
# print(jam)

list_of_names = ["steve", "dwayne", "freya", "nelson", "sam", "john", "abu", "binta"]
# filters = filter(lambda a :"a" not in a , list_of_names)
# jam = list(filters)
# print(jam)
# -------------------------------------------------------------------------
# getdata = input()
# print(getdata)

# tee = getdata.split(" ")
# print(tee)

# tea = map(lambda d: int (d), tee)
# tes = list(tea)
# print(tes) 

# tes.sort()
# print(tes)

# tre = tes[-2]
# print(tre)

# --------------------11/11/2021 CLASS------------------------------------------

# se = ["22", "33"]
# sa = str(se)
# print(sa)
# print(type(sa))
# ee = sa[1]
# print(ee)

# BUILT-IN MODULES
## TIME
# import time

# print("this is line 91")
# time.sleep(20)
# print("this is line 93")  

## RANDOM
import random as rd
# rd.seed(99)
# print(list_of_names)
# rd.shuffle(list_of_names)
# LINE 100 IS TO CREATE A BLANK SPACE
# print("\n")
# print(list_of_names)
# print("\n")

# rd_pick = rd.choice(list_of_names)
# print(rd_pick)

r_sample = rd.sample(list_of_names, k = 2)
print(r_sample)

# r_range = rd.randrange(9,23,3)
# print(r_range)

## DATETIME
# from datetime import datetime as dt
# from time import strptime
# METHOD 1 = .now()
# current_dt = dt.now()
# print(current_dt)
# current_dt = dt.now().hour
# current_dt = dt.now().minute
# current_dt = dt.now().month
# current_dt = dt.now().year
# current_dt = dt.now().second

# METHOD 2 = .strftime()
# current_dt1 = current_dt.strftime("%x")
# print(current_dt1)

# METHOD 3 = .strptime()
# fake_date = "9/4/2021"

# real_date = dt.strptime(fake_date, "%d/%m/%Y")
# # print(real_date)

# notable_days = ["01/01/2021", "15/01/2021", "14/02/2021", "01/04/2021", "29/05/2021", "12/06/2021", "01/10/2021", "25/12/2021", "26/12/2021"]

# noting_days = list(map(lambda a : dt.strptime(a, "%d/%m/%Y"), notable_days))
# print(list(noting_days))
# red = (list(noting_days[0]))
# print(noting_days[0])

### CONDITIONALS
# if 77> 77:
#     print("Yes")
# else:
#    print("No")

# task1 = input()
# print(task1)

# task2 = set(task1)
# print(task2)

# if len(task1) == len(task2):
#     print("There are no duplicates")
# else:
#     print("There are duplicates")

# gret = input()

# if int(gret) % 2 == 0:
#    print("even number")
# else:
#    print("odd number")

# if int(gret) % 2 == 0 and int(gret)> 20:
#     print("Both conditions are met")
# else:
#     print("They were not met")

# if int(gret) % 2 == 0 and int(gret)> 20:
#     print("Even number and greater than 20")
# elif int(gret) % 2 != 0 and int(gret)> 20:
#     print("Odd number and greater than 20")
# else:
#     print("Number is less than 20")

# cracker = 0
# while (cracker < 5):
#     print("cracker is less than 5")
   
#     cracker += 1

# to use the keyword 'break'
# cracker = 0
# while cracker < 5:
#     if cracker == 3:
#         print("This is my ride outta the loop")
#         break
#     else:
#         print("cracker less than 5")
#         cracker +=1


# TASK

# get_password1 = input("Enter password here:")
# while True:
#     get_password2 = input("Repeat password here:")
#     if get_password1 == get_password2:
#         print("Sign up successful!")
#         break
#     else:
#         pass

# get_password_1 = input("Enter password here:")
# limit = 0
# while limit < 2:
#     get_password_2 = input("Repeat password here:")
#     if get_password_1 == get_password_2:
#         print("login successful:")
#         break
#     elif limit == (2 - 1):
#         print("WRONG! Please Try Again After 30 Minutes.")
#         break
#     else:
#         print("WRONG!!!")
#         limit += 1

# TASK: While Loop: create a guess game. 
# figure = input("input figures here:")
# figure = figure.split(" ")
# fig = map(lambda a: int(a), figure)
# fid = list(fig)
# print(fid)

# import random as rd
# rand = rd.randrange(fid[0],fid[1])
# # print(rand)

# while True:
#     guess_number = input("Guess number:")
#     guess_number = int(guess_number)
#     if guess_number == rand:
#         print("YOU WIN!!!")
#         break
#     elif guess_number < rand:
#         print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
#     elif guess_number > rand:
#         print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
#     else:
#         pass


# FOR LOOP
# SYNTAX: for item in iterable
#               BLOCK OF CODE(this is usually the print statement)
# *item* serves as a temporary variable name for each and every member/item in the iterable
# The for loop runs for as many times as the number of items in an iterable

# e.g 1: This is INDEPENDENT
# entry_data = "Universe"
# for a in entry_data:
#     print("home for all")

# e.g 2: This is DEPENDENT
# new_list = ["pop", "rock", "country"]
# for item in new_list:
    # print(item)

# FOR LOOP with enumerate
# names = ["sheldon", "penny", "howard", "leonard", "rajesh"]
# for index, item in enumerate(names):
#     print(item,item)

# TASK: create a program that performs a 10% increase on odd numbers and 10% decrease on even numbers inputed by the user
# terf = input()
# terf = terf.split(" ")
# terf = map(lambda w :int(w), terf)
# tref = list(terf)
# print(type(tref))
# num = 0
# print(type(num))
# tref[num] = tref[num] - (tref[num] * 0.1)

# INCOMPLETE(INCORRECT)
# for num in tref:
#     if tref[num] % 2 == 0:
#         tref[num] = tref[num] - (tref[num] * 0.1)
#         print(tref[num])
#         num += 1
#     elif tref[num] % 2 != 0:
#         tref[num] = tref[num] + (tref[num] * 0.1)
#         print(tref[num])
#         num += 1
#     else:
#         pass
    

# for solution 2
# for index, entry in enumerate(tref):
#     if entry % 2 == 0:
#         tref[index] = 0.9 * entry
#         print(tref[index])
#     elif entry % 2 != 0:
#         tref[index] = 1.1 * entry
#         print(tref[index])
#     else:
#         pass



# get_data = input()
# con_list = get_data.split(" ")
# lens = len(con_list)
# print(lens)
# real_integers = list(map(lambda a : int(a), con_list))
# real_odd = list(filter(lambda a: a % 2, real_integers))
# print(real_odd)
# real = len(real_odd)

# real_even = lens - real
# print(f"there are {real} odd numbers.")
# print(f"there are {real_even} even numbers.")

# odd = 0
# even = 0
# for entry in real_integers:
#     if entry % 2 == 0:
#         even += 1
#     elif entry % 2 != 0:
#         odd += 1
#     else:
#         pass

# print("there are {} odd numbers".format (odd))
# print(f"there are {even} even numbers")

# inputs = input()
# inputsd = inputs.split()
# inpu = "".join(inputsd)
# print(inpu)
# lend = len(inpu)
# inp = list(filter(lambda a : a.isalpha(),inpu))
# print(inp)
# land = len(inp)
# ans = lend - land
# print(f"there are {land} letters")
# print(f"there are {ans} digits")

# gett = 10000000
# ger = str(gett)
# gre = list(map(lambda a : a.isdigit(), ger))
# grt = len(gre)
# print(grt)

# gret = 49674647.9995
# gret = str(gret)
# grew = gret.replace(".", "")
# gret = gret.split(".")
# gty = "".join(gret)
# print(len(gty))
# gre = list(map(lambda a : a.isdigit(), grew))
# print(gre)
# grt = len(gre)
# print(grt)



# digit = 0

# if "." in gret:
#     print(len(gret) - 1)
# else:
#     print(len(gret))

# TASK: write a program that takes in integers from the user and print them one after the other in reverse order
# rice = input()
# price = rice.split(" ")
# price = list(price)
# price.reverse()
# print(price)

# TASK: write a program that takes in a date:- 25/12/2021 converts it to an actual date and add the time.
from datetime import datetime as dt
# dates = input()
# print(dates)
# date = dt.now().hour
# print(date)
# date = str(date)
# dat = dt.now().minute
# dat = str(dat)
# print(type(dat))
# dae = dt.now().second
# dae = str(dae)
# dan = dates + "/" + date + "/" + dat + "/" + dae
# print(dan)
# real = dt.strptime(dan, "%d/%m/%Y/%H/%M/%S")
# print(real)


# TASK: write a program that takes in "Jun 12 2021 3:30PM" and turns it into an actual date and time.
# task = input()
# rate = dt.strptime(task, "%b %d %Y %H:%M%p")
# print(rate) 






