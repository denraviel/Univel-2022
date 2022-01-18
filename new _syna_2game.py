from os import name
import random as rd
import csv
import time
#set play limit to 10 tries then delay game for 10 seconds
def collect_data():
    figure = input("input figures here \n: ")
    name = input("input name \n: ")
    figure = figure.split(" ")
    fig = map(lambda a: int(a), figure)
    fid = list(fig)
    # print(fid)
    rand = rd.randrange(fid[0],fid[1])
    return rand,name
def play():
    tries = 0
    limit = 0
    rand,name = collect_data()

    while True:
        guess_number = input("Guess number:")
        guess_number = int(guess_number)
        tries +=1 # increment tries at every tries
        limit +=1 
        if guess_number == rand:
            print("YOU WIN!!!")
            break
        elif guess_number < rand:
            print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
        elif guess_number > rand:
            print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
        if limit ==4:
            print("you missed it :",tries,"times")
            print("Try again in 4 seconds")
            limit = 1
            time.sleep(4)
    # write_to_files(name,tries)
    # print("you tried: ",tries,"time(s)")
    # return(name,tries)


    
        
# def write_to_files(name, tries):
#     # name,tries= play()
#     with open("data.csv","a", newline="") as our_log_file: #context manager
#         pen=csv.writer(our_log_file)
#         pen.writerow(["Name" , "Tries"])
#         our_log_file.write(f"{name},{tries}\n")
play()

