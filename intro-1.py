#Creating my first Python variable
new_user_data = {
    "name" : "Charles",
    "age" : 50,
   "gender": "male"

}
new_int = 99
# Using my first Python Print function 

#print(new_user_data)

#my_info2 = {"name" : ["Musa", "Amina"], "gender": ["Male", "Female"], "age": [50,79]}
x = 4
x = "James"
# print(x)
# Casting in Python

p = int(4)
y = str(4)
r = float(4)
# print(p,y,r) 
# print(type(p),type(y),type(r))
#
#LOGICAL OPERATORS IN PYTHON
final_verdict = not((54 <=42) or (60 != 60)) or (("Rain" == "rain") and not(82.2 >= 82.2))
#
# print(final_verdict)
# IDENTITY OPERATORS
# is and is not check for the similar memory locations i.e the variable names
# 
# MEMBERSHIP OPERATORS 
# ITERABLES
# Strings, list, tuple, set, dict
# 
# in and not in check if the values are present in the specified object
# NOTE: A white space is a valid string entry

feedback = 20 is 200
# print (feedback)
first = [29, "True","Sunny"]
first = [9, "True","Sunny"]
output = first == first

check_member = "oy" in "money makes the world go round!"
print(check_member)


# STRINGS
# Slicing [start:stop:step] default start is 0, default stop is last item, to skip one interval aplly step 2
# NOTE: The 
first_phrase = "The boy"
second_phrase = "in my class is handsome"
full_sent = first_phrase + " " + second_phrase
# print(full_sent)
new_chunk = full_sent[-23:-12]
# print(new_chunk)
# print('hello World')

#STRING FORMATTING 

# Using the format method
climate = "sunny" # This is the dynamic weather variable
temperature = 39 # This the dynamic temperature variable
weather_report = "its quite {} with a temperature of {}".format(climate,temperature) # We want the climate and temperature to be dynamic
# print(weather_report)

# Using f string
weather_report2 = f"It is quite {climate} with a temperature of {temperature}"
# print(weather_report2)



