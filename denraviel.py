# new_word = "strength"
# print (new_word [  : 2])
# num = 60
# num += 7
# print(num)


final_verdict=not((58<=42) or (60!=60)) or (("Rain==rain")) and not(82.2>=82.2)
# print(final_verdict)
# weather = "sunny"
# temperature = "39 degrees"
# weather_report = "it is quite {} with a temperature of {}".format(weather, temperature)
# print(weather_report)

# weather_report2 = f"it is quite {weather} with a temperature of {temperature}"
# print(weather_report2)


# #escape you use the (\)

# source_of_income = 'the nation\'s crude oil'
# print(source_of_income)


# # title()

new_weather_report = "it is quite sunny despite the downpour all through the night"
# mod_one = new_weather_report.title()
# print(mod_one)

# ##startswith and endwith always returns with boolean
# mod_two = new_weather_report.startswith("it")
# print(mod_two)

# #index()

# mod_three = new_weather_report.index("night")
# print(mod_three)



# #find
mod_ex= new_weather_report.find("a")
# print(mod_ex)



# #split

# mod_four = new_weather_report.split(" ")
# print(mod_four)


# mod_ter = new_weather_report.split("downpour")
# print(mod_ter)




# #join- 

# mod_five = "-".join(mod_four)
# print(mod_five)


# #count

# mod_six = new_weather_report.count("the")
# print(mod_six)

# #replace

# mod_seven = new_weather_report.replace("p", "f")
# print(mod_seven)

# #strip there bis lstrip and rstrip. lstrip is leading and rstrip is trailing

mod_eight = new_weather_report.lstrip("it is quite sunny")
# print(mod_eight)




# #for rstrip
# mod_nine = new_weather_report.rstrip("t")
# print(mod_nine)


# new_collection = [6, True,12,9,False,"name","Bentley","Football",9.7,None,8.5]
# desired_items = new_collection[4]
# # print(desired_items)


# desired_portion = new_collection [-6: -2: 2]
# # print(desired_portion)

# #changing data 

# new_collection[5] = "school"
# print(new_collection)


# # new_collection[1 : : 3] = ["money", "food", "ikoyi", "glass"]
# print(new_collection)
 


# #join Lists

# first_list=[3,6,7]
# second_list=[8,9,8]
# join_list=first_list + second_list
# print(join_list)
# #clear 

# #count


# #extend
# sports = ["baxsketball", "boxing", "swimming",]
# stars = ["Kobe Bryant", "Mike Tyson", "Micheal Phelps"]
# sports.extend(stars)
# print(sports)

# #remove
# new_collection.remove(9)
# print(new_collection)

# #append
# new_collection.append("Biscuit")
# print(new_collection)

# #copy  copies the item from the variable choosen
# backup_collection =new_collection.copy()
# print(backup_collection)

# #insert
# new_collection.insert(2, "brothers")
# print(new_collection)

# #sort it works for a list that has one set/kind of data example for just strings 




# ##Tuples you cant change an item in a tuple rather you can extend a tuple
scores = (58, 73, 85, 67)
desired_score=scores[-1]
# print(desired_score)


# #set use curly braces for a set
grocery_cart1={"ham", "Burger", "yoghurt", "Eggs", "Cookies", "Bread", "Sausage"}
# grocer_cart2 ={"Beverages", "Cookies", "Wine", "Frozen Turkey", "Burger", "Eggs"}
# # print(grocery_cart1)
# # print(grocer_cart2)

# # #discard
# # grocery_cart1.discard("ham")
# # print(grocery_cart1)

# # #union
# # full_cart = grocery_cart1.union(grocer_cart2)
# # print(full_cart)

# #update
# # full_cart = grocery_cart1.update(grocer_cart2)
# # print(full_cart)


# #difference_update
# # grocer_cart2.difference_update(grocery_cart1) 
# # print(grocer_cart2)

# # common_groceries = grocery_cart1.intersection(grocer_cart2)
# # print(common_groceries)

# # grocery_cart1.symmetric_difference_update(grocer_cart2)
# # print(grocery_cart1)






# ##DICTIONARY
# customer_info = {
#     "name" : ["Adam Freeman", "Alissa Banks", "Ngozi Chukwuma","John Doe"], "gender" : ["male","female", "female", "male"], "nationality" : ["American", "Canadian", "Nigerian", "British"]

# }
# # print(customer_info)
# all_names = customer_info["name"]
# # print(all_names)

# #indexing to change name

# all_names[2] = "Ngozi Nnamdi"
# # print(customer_info)

# all_nationalities = customer_info.get("nationality")
# # print(all_nationalities)

# #items for dictionaries

# all_enteries = customer_info.items()
# # print(all_enteries)

# #update for dict
# # customer_info.update({"age" : [31, 24, 30, 22]})
# # # print(customer_info)


# # ###Built in Functions

# # #input
# # get_data = input()
# # # print(get_data)
# # fer = get_data.split(" ")
# # # print(fer)
# # ger = int(fer[0])
# # ger2 = int(fer[1])
# # average = (ger +ger2)/2
# # # print(average)


#  #9/11/2021
# #zip
# name = ["john", "dave", "bill"]
# age = [22, 24, 26]
# gore = zip(name,age)
# # print(gore)
# # p= print(list(gore))


# # output = list(gore)
# # print(output)

#  #if you are zipping two iterables of diffrent length you will have a zipped that is the length of the smaller iterables
#  #enumerate
 
# # artist = ["drake", "Burna boy", "ckay"]
# # reply = enumerate(artist)
# # # print(list(reply))

#lambda- lamda parameter :expressions
# my_multi = lambda x : x*3+500-9
# output9 = my_multi(10000)
# print(output9)



# # great = lambda x, y, z :x*2-y
# # free = great(20, 30, 40)
# # # print(free)

# # checker = lambda a : a.startswith("is")
# # used = checker("This is just a baby string")
# # # print(used)

# # #map()  map(fun,iter) 
# # ##fun= is a function to which a map passes each element of a given iterable
# # ###iter=  It is a iterable which is to be mapped
# # upgraded_scores = map(lambda a : a + 2, scores)
# # # print(list(upgraded_scores))


list_of_names = ["fred", "kozzo","george","magic"]
greed = map(lambda a : a.title (),list_of_names)
# print(list(greed))


# # #filter

# care =[20, 31, 45, 60, 10, 77]
# rends = filter(lambda a : a % 2==0, care)
# print (list(rends))





list_of_names2 = ["steve", "dwayne", "freya", "nelson", "sam", "john","abu", "binta"]
# #expression does not allow assignment operators in Lambda 
# fred = filter(lambda r :"a" not in r , list_of_names2)
# # print(list(fred))


# # #range(start,stop,step) there is no default for stop in range
# dream= range(-5,-1,2)
# print(list(dream))


# troy = input("Enter data here:")
# con = troy.split(" ")
# newp = list(map(lambda a : int(a), con))

# brief = list(set(newp))
# brief.sort()

# core = brief[-2]
# print(core) 



##assignment corrected 2e


# my_data = (51,69,64,30,79,20,4,90)
# step_one = list(my_data)
# step_one.sort()
# needed_integer=step_one.pop(5)
# step_one.insert(2, needed_integer)

# step_two = tuple(step_one)
# # print(step_two)

## 11/11/2021
greesd = str(["30", "33"])
# print(greesd)
# print(type(greesd))

d= greesd[0]
# print(d)

#built in modules to use modules you have to import them
##time (.sleep method)=time.sleep() take in argument which is usually an integer
import time
# print("this is line 316")
# time.sleep(30)
# print("this is 318")

##random (.shuffle method)= random or alias rd.shuffle() takes into argument the variable 
import random as rd
rd.seed(99) 
# print(list_of_names2)
# rd.shuffle(list_of_names2)
# print("\n")
# print(list_of_names2)


#(.chioce method) randomly selects item in an iterable
# print(list_of_names2)
# print("\n")
trigger= rd.choice(list_of_names2)
# print(trigger)


#(.sample method)
# print(list_of_names2)
# print("\n")
# forte = rd.sample(list_of_names2, k = 2)
# print(forte)

#(.randrange method)
# print("\n")
# random_quirk= rd.randrange(9, 23, 3)
# print(random_quirk)


#(.seed method)

##datetime module
from datetime import datetime as dt
#(.now method)
# current_time = dt.now()
# print(current_time)

#(.now. year or hour or month or minutes or seconds)
# pringles = current_time.year
# print(pringles)


#(.strftime method)
# free_mode = current_time.strftime("%A")
# print(free_mode)  
# free_mode1 = current_time.strftime("%a")
# print(free_mode1)



# #(.strptime method "%d/%m/%y", %H:%M:%S)
fake_date = "9/4/2021"
form = dt.strptime(fake_date, "%d/%m/%Y")
# print(form)


# notable_days = ["01/01/2021", "15/01/2021", "14/02/2021", "01/04/2021", "29/05/2021","12/06/2021", "01/10/2021","25/12/2021", "26/12/2021"]
# grip = list(map(lambda a : dt.strptime(a ,"%d/%m/%Y"), notable_days))
# # print(list(grip)) 
# # frost = list(grip)
# print(grip[0])

#conditionals  if/elif/else statements
#if conditional

# if 88 > 87:
#     print("yes")
# else:
#     print("no")

# prefer = input("information:")
# if len(prefer)==len(set(prefer)):
#     print("there are no duplicate")
# else:
#     print("there are duplicate")






# 




#elif if you are checking for multiple conditions with diffrent block of codes. if there is a segment checking several conditions let the highest appear 1st

# greedy_data = input("data here :")
# if int(greedy_data) % 2 == 0 and int(greedy_data) > 20 :
#     print("even number and greater than 20")
# elif int(greedy_data) % 2 !=0 and int(greedy_data) > 20:
#     print("odd number and greater than 20")
# else:
#     print("number is less than 20")


###loops ther are two types of loop, the while loop and for loop
#while loop
#while (condition is met)

  #repeats the block of code

# cracker = 0
# while(cracker < 5):
#     print("cracker is less than 5 ")
#     cracker += 1

# question 1
# wild_integers = input("Enter data here: ")
# print(wild_integers)

# step_one =wild_integers.split(" ")
# print(step_one)
# step_two= list(map(lambda g : int(g),step_one))
# print(step_two)

# Even_integers, Odd_integers = 0, 0
# numeric = 0
# while(numeric <len(step_two)) :
#   if step_two[numeric] % 2 == 0:
#     Even_integers += 1
#   else:
#     Odd_integers += 1
#   numeric += 1
# print( Even_integers)
# print( Odd_integers)


#November162021
##loops(cont.)
#unending while loop looks like;
#  while true:
    #block of code.....
    # ......the only way to stop and indefinite code is to break it

#Example of when to use break
# cracker = 0
# while (cracker<5):
#   if cracker == 3 :
#     print("this is my ride out")
#     break
#   else:
#     print("cracker is less than 5")
#     cracker += 1




# get_password1 = input("Enter password: ")
# while True:
#   get_password2 = input("repeat password :")
#   if get_password1== get_password2:
#     print("sign up sucessful")
#     break
#   else:
    # pass



# get_real_password = input("enter real password: ")
# limit= 0
# while(limit < 2):
 #   get_real_password2 = input("reset password here: ")
#   if get_real_password==get_real_password2:
#     print("login successful")
#     break
#   else:
#     limit+=1


#task 1
# numbers= input("input the number: ")
# print(numbers)

# step_one = numbers.split(" ")
# print(step_one)
# step_two = list(map(lambda r:int(r),step_one))

# import random as rd
# frost = rd.randrange(step_two[0],step_two[1])
# print(frost)

# while True:
#   frost6 = input("the number: ")
#   frost7 = int(frost6)
#   print(frost7)
#   if frost7==frost:
#     print("you win")
#     break
#   elif frost < frost7:
#     print("hint : your number is lower")
#   elif frost > frost7:
#     print("hint: your number is higher")
#   else:
#     pass

#for loop
###range , zip and enumerate are also iterables


names = ["sheldon", "penny", "howard", "leo", "raj"]
# for money,kudi in enumerate(names):
#   print(kudi,money) 
# de = [(index,entry) for index, entry in enumerate (names)]
###task2
# print(de)
# numbers= input("input the number: ")
# print(numbers)

# step_one = numbers.split(" ")
# print(step_one)
# step_two = list(map(lambda r:int(r),step_one))
# for index, entry in enumerate(step_two):
#   if entry % 2 == 0:
#     step_two[index] = 0.9 * entry
#     print (step_two[index]) 
#   elif entry % 2 != 0:
#     step_two[index] = 1.1 * entry
#     print(step_two[index])
#   else:
#     pass

##18 november
#assignment correction
# get_dara = input("enter integers here: ")
# conlist = get_dara.split(" ")
# print(conlist)
# real_integers = list(map (lambda a : int(a), conlist))
# print(real_integers)
# nextlevel= list(filter(lambda a : a % 2 ,real_integers))
# print(nextlevel)
# no_of_input = len(real_integers)
# no_of_odd = len(nextlevel)
# no_of_even = no_of_input - no_of_odd
# print(f"there are {no_of_odd} odd numbers")
# print(f"there are {no_of_even} even numbers")




# data_guy = 1.676786
# dtes = str(data_guy)
# print(dtes)
# nutts = dtes.split (".")
# print(nutts)
# drep = "".join(nutts)
# print(drep)

# ferry = list(map(lambda a : a.isdigit(), drep))
# print(ferry)
# sapa = len(ferry)
# print(sapa)

#rt
# dundy = input(" this integer : ")
# sulve = dundy.split(" ")
# steo = list(sulve)
# steo.reverse()
# print(steo)



# dagger = input("date input :")
# print(dagger)

# date = "June 12 2021 3:30pm " 


#23 november
#list comprehension 
#[expression for item in iterable] 
#example:
# scoring = [42, 53, 61, 81, 57]
# upgraded_scores = [num + 2 for num in scoring]
# print(upgraded_scores)



#sorted built in function
# tred = [("high" , 3),("low", 2), ("nan", 6) ]
# inter = sorted(tred, key=lambda a:a[1])
# print(inter)






#File i/o we will be working 
























 











  
   

 










 

  














 





















    





























 







