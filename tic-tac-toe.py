board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}" , end= "")
        print()
print_board(board)

def quit(input_user):
    if input_user == "q": 
        return True
    else :
        return False
def check(input_user):
    if not isnum(input_user) : return False
    input_user = int(input_user)
    if not bounds(input_user) : return False

    return True
    #ijj
def isnum(input_user):
    if not input_user.isnumeric():
        print("Not a valid number")
        return False
    else: return True

def bounds(input_user):
    if input_user > 9 or input_user < 1:
        print("Out of bound")
        return False
    else:
        return True

def istaken(input_user):  



while True:
    input_user = input("please enter a position from 1 to 9 or \"q\" to quit:")
    if quit(input_user):
        break
    if not check (input_user):
        print("try again")
        continue
