import time



# for i in range (20):
#     print(i)
#     time.sleep(1)

# for t in range (10):
#     for p in range (10):
#         print(t, ":" ,p)
#         time.sleep(1)


# for m in range(10):
#     for r in range(10):
#         for w in range(60):
#             for z in range(60):
#                 print(m,":",r,":",w,":",z)
#                 time.sleep(1)



# for m in range(10,0,-1):
#     for r in range(10,0,-1):
#         for w in range(10,0,-1):
#             for z in range(10,0,-1):
#                 print(m,":",r,":",w,":",z)
#                 time.sleep(1)


# for d in range(1, 1000):
#     sum_num = d + d + d
#     place_holder = str(d)[-1]
#     triple_holder = place_holder * 3
#     thor = int(triple_holder)
#     if thor == sum_num:
#         print ("hurray num is :",d,"->",sum_num)
#         break
#     print(d,sum_num,place_holder,triple_holder)
   

# def r():
#     print(677+45)
# r()
    


# def r(d):
#     print(d+56)
# r(3444)
#d is an argument and print(d+56) is the statement

# def use():
#         for m in range(10):
#             for r in range(10):
#                 for w in range(60):
#                     for z in range(60):
#                         print(m,":",r,":",w,":",z)
#                         time.sleep(1)
# use()




# def use(hours, mins, secs):
#     for m in range(hours+2):
#         for r in range(mins+2):
#             for w in range(secs+2):
#                 print(m,":",r,":",w)
# use(2,10,6)


       


# def increment(num):
#     return num +3

# def userr(hours, mins, secs):
#     for o in range(increment(hours)):
#         for g in range(increment(mins)):
#             for q in range (increment(secs)):
#                 print(o,":",g,":",q )
# userr(2, 10, 6)



def increment(num):
    return num +3

def restructure(hours, mins,secs):
    return f"{hours} hours {mins} mins {secs}secs"
    
def userr(hours, mins, secs):
    for o in range(increment(hours)):
        for g in range(increment(mins)):
            for q in range (increment(secs)):
                print(restructure(o,g,q ))
userr(2, 10, 6)


