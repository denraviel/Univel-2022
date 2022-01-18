# figure = input("input figures here: ")
# figure = figure.split(" ")
# fig = map(lambda a: int(a), figure)
# fid = list(fig)
# print(fid)

# import random as rd
# rand = rd.randrange(fid[0],fid[1])
# # print(rand)
# tries = 0
# while True:
#     guess_number = input("Guess number:")
#     guess_number = int(guess_number)
#     tries +=1
#     if guess_number == rand:
#         print("YOU WIN!!!")
#         break
#     elif guess_number < rand:
#         print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
#     elif guess_number > rand:
#         print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
#     else:
#         pass
# print("you tried: ",tries,"times")



figure = input("input figures here \n: ")
name = input("input name \n: ")
figure = figure.split(" ")
fig = map(lambda a: int(a), figure)
fid = list(fig)
# print(fid)

import random as rd
rand = rd.randrange(fid[0],fid[1])
# print(rand)
tries = 0
while True:
    guess_number = input("Guess number:")
    guess_number = int(guess_number)
    tries +=1
    if guess_number == rand:
        print("YOU WIN!!!")
        break
    elif guess_number < rand:
        print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
    elif guess_number > rand:
        print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
    else:
        pass
print("you tried: ",tries,"times")

# import random as rd
# def collect_data():
#     figure = input("input figures here \n: ")
#     name = input("input name \n: ")
#     figure = figure.split(" ")
#     fig = map(lambda a: int(a), figure)
#     fid = list(fig)
#     print(fid)
#     rand = rd.randrange(fid[0],fid[1])
#     return rand,name
# def play():
#     tries = 0

#     rand,name = collect_data()

#     while True:
#         guess_number = input("Guess number:")
#         guess_number = int(guess_number)
#         tries +=1
#         if guess_number == rand:
#             print("YOU WIN!!!")
#             break
#         elif guess_number < rand:
#             print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
#         elif guess_number > rand:
#             print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
#         else:
#             pass 
#     return name,tries


# #     print("you tried: ",tries,"times")
# # play()

        

# def write_to_files(name, tries):
#     with open("database.csv","a") as our_log_file:
#         name = "atha"
#         tries = 6
#         our_log_file.write(f"{name},{tries}\n")
#     print("logged session")
# write_to_files("dami", 20)