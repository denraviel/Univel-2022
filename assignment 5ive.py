
from datetime import datetime as dt


read_file = open("C:/users/denra/Documents/python/Rawfile.txt", mode="r",encoding= "utf-8")
whole_data = read_file.readlines()   

refined_data =[entry.rstrip("\n") for entry in whole_data]


sorted_refined_list = sorted(refined_data, key=lambda a : dt.strptime(a.split(" on ")[1], "%d-%m-%Y"))

list_of_names =[]
list_of_sales =[]
list_of_dates =[]

for entry in sorted_refined_list:
    extracted_names = entry.split(" : ")[0]
    list_of_names.append(extracted_names)

    extracted_sales = int(entry.split(" ")[3].lstrip("₦"))
    list_of_sales.append(extracted_sales)

    extracted_dates = entry.split(" ")[5].replace("-", "/")
    list_of_dates.append(extracted_dates)
    
    # print(list_of_names)
    # print(list_of_dates[5:])
    # print(list_of_sales[5:])


#Question A
name_sales= {}
for name, amount in zip(list_of_names,list_of_sales):
    name_sales[name]= name_sales.get(name,0)+ amount
# print(name_sales)

sorted_new = dict(sorted(name_sales.items(), key = lambda a : a[1],reverse=True))
# print(sorted_new)
det = list(sorted_new)
# print(det[:10])



#Question B
m = list(map(lambda a: str(a), list_of_dates))
# print(m)

fx = list(map(lambda s : s.split("/")[1], m))
# print(fx)
efx = list(map(lambda t: dt.strptime(t, "%m"), fx))
# print(efx)
fluxx = list(map(lambda r:r.strftime("%B"), efx))
# print(fluxx)
work_please = {}
for month, amount in zip(fluxx , list_of_sales):
    work_please[month] = work_please.get(month, 0) + amount
tally = [(key, values) for key, values in work_please.items()]
# print(tally) 

#Question C
sales = sorted(tally, key = lambda a: a[1])
print(sales)
low_sales =  sales[0]
high_sales = sales[-1]
print("The month with lowest sales :", low_sales)
print("the month with highest sales :", high_sales)

#Question D
agent_names = list(sorted_new.keys())
agent_sales = list(sorted_new.values())
agent_commision = [amount* 0.055 for amount in agent_sales]
total_sales = sum(agent_sales)
agent_contribution = list(map(lambda a : str(round((a/ total_sales)* 100,3))+ "%", agent_sales))
dict_4_sales = {}
for names, commission in zip(agent_names, agent_commision):
    dict_4_sales[names] = dict_4_sales.get(names, 0) + commission
print(dict_4_sales)

