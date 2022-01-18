# creator = input("Run my code here: ")
# creator2 = creator.split(" ")
# dodge = list(set (map (lambda a : int(a),creator2)))
# print(dodge)

# dodge.sort()
# cred = dodge[3]
# print(cred)


# kach = [(a) for a in range(100,161)]



#practive


get_dara = input("enter input here: ")
conlist = get_dara.split(" ")
print(conlist)
new_string = "".join(conlist)
print(new_string)
frok = len(new_string)
frok2 = list(filter(lambda a : a.isalpha(), new_string))
this = len(frok2)
ans = frok - this
print(f" there are {this} letters")
print(f"there are {ans}  digits")








