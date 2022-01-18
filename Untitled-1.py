#question 1
wild_integers = input("Enter data here: ")
print(wild_integers)

step_one =wild_integers.split(" ")
print(step_one)
step_two= list(map(lambda g : int(g),step_one))
print(step_two)

Even_integers, Odd_integers = 0, 0
numeric = 0
while(numeric <len(step_two)) :
  if step_two[numeric] % 2 == 0:
    Even_integers += 1
  else:
    Odd_integers += 1
  numeric += 1
print( Even_integers)
print( Odd_integers)