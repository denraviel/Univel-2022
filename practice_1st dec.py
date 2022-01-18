from os import name
import random as rd
import csv
def collect_data():
    figure = input("input figures here \n: ")
    name = input("input name \n: ")
    figure = figure.split(" ")
    fig = map(lambda a: int(a), figure)
    fid = list(fig)
    print(fid)
    rand = rd.randrange(fid[0],fid[1])
    return rand,name
def play():
    tries = 0

    rand,name = collect_data()

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
    write_to_files(name,tries)
    print("you tried: ",tries,"time(s)")
    # return(name,tries)



    
        

def write_to_files(name, tries):
    # name,tries= play()
    with open("data.csv","a", newline="") as our_log_file: #context manager
        pen=csv.writer(our_log_file)
        pen.writerow(["Name" , "Tries"])
        our_log_file.write(f"{name},{tries}\n")
play()


   