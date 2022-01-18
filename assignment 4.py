#Question A
lsr=[]

numbers= input("input the number: ")
print(numbers)
step_one = numbers.split(" ")
sector = int(step_one[0])
sector2 = int(step_one[1])
print(sector)
# print(sector2)

# for soulfood in range(sector, sector2):
#     s= str(soulfood)
#     if (int(s[0])%2!=0) and (int(s[1])%2!=0) and (int(s[2])%2!=0):
#         lsr.append(s)
# print( ",".join(lsr))




#Question B

# main_digits = int(input("this are the digits: "))
# reverse_digit = 0
# while (main_digits> 0):
#     rem = main_digits % 10
#     reverse_digit = (reverse_digit* 10) + rem
#     main_digits = main_digits // 10
# print("The reverse number is : {}".format(reverse_digit))


#Question C

# letters = input("Hot ones: ")
# listed_letters = list(letters)
# print(listed_letters)
# listed_letters.sort(reverse=True)
# print(listed_letters)
# Joined_letters = "".join(listed_letters)
# print(Joined_letters)
# one_string= str(Joined_letters)
# print(one_string)


#Question D
set_4u = {55, 99, 77, 44, 33, 88, 11, 66}
set_leftus = print(set(list(filter(lambda a :a % 2, set_4u))))

info = []
info.append([sneaker_brand,sneaker_description,sneakers_old_price,new_price_range_one,new_price_range_two,sneakerd_new_price,d_discount,sneaker_rating])
with open ("jumia_sneaker.csv", "w",newline="") as f:
    writer = csv.writer(f)
    headers = ["sneakerbrand","sneakerdescription","sneakersoldprice,","newpricerangeone","newpricerangetwo","new price","discount", "rating"]
    for data in info:
        writer.writerow(data)