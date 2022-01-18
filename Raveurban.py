from datetime import datetime as dt
import csv
import xlwt
from tempfile import TemporaryFile as TF

read_file = open("C:/users/denra/Documents/python/Rawfile.txt", mode="r",encoding= "utf-8")
whole_data = read_file.readlines()
# print(whole_data[:5])
## to remove the unwanted "\n" from eveery entery in the data
refined_data =[entry.rstrip("\n") for entry in whole_data]
# print(refined_data)

# we sort the data with respect to the date

sorted_refined_list = sorted(refined_data, key=lambda a : dt.strptime(a.split(" on ")[1], "%d-%m-%Y"))
print(sorted_refined_list[-5:])

#we then use a for loop  to 
list_of_names =[]
list_of_sales =[]
list_of_dates =[]

for entry in sorted_refined_list:
    extracted_names = entry.split(" : ")[0]
    list_of_names.append(extracted_names)

    extracted_sales = int(entry.split(" ")[3].lstrip("₦"))
    list_of_sales.append(extracted_sales)

    extracted_dates = entry.split(" on ")[1].replace("-", "/")
    list_of_dates.append(extracted_dates)
    
    # print(list_of_names)
    # print(list_of_dates)
    # print(list_of_sales)

#the newline just inserts an empty string
new_file = open("C:/users/denra/Documents/python/Raveurban.csv", mode="w", encoding="utf-8", newline="")
#create a pen to write into csv for new_file
pen=csv.writer(new_file)
#the first row is the header:
pen.writerow(["names", "sales", "date"])

for x in range(len(sorted_refined_list)):
    pen.writerow([list_of_names[x], list_of_sales[x],list_of_dates[x]])

new_file.close() 

# agents = len(set(list_of_names))
# print(agents)

new= {}
for name, amount in zip(list_of_names, list_of_sales):
    new[name]= new.get(name,0)+ amount
# print(new)

# sort with respect to their names
sorted_names_sales = dict(sorted(new.items(), key = lambda a : a[0]))
print(sorted_names_sales)

# FIRST EXCEL SHEET DATA
agent_names = list(sorted_names_sales.keys())
agent_sales = list(sorted_names_sales.values())
agent_commission = [amount * 0.055 for amount in agent_sales]
total_sales = sum(agent_sales)
agent_contribution = list(map(lambda a : str(round((a /total_sales) * 100, 3)) + "%", agent_sales))

# SECOND EXCEL SHEET DATA
total_commission = sum(agent_commission)
total_revenue = sum(agent_sales)
net_revenue = total_revenue - total_commission


# GETTING THE BOOK 
book = xlwt.Workbook()

# ADDING THE SHEET 
first_sheet = book.add_sheet("agents' records")
second_sheet = book.add_sheet("net income")

# WRITTING INTO THE FIRST SHEET 
first_sheet.write(0, 0, "agent name")
first_sheet.write(0, 1, "agent sales")
first_sheet.write(0, 2, "agent commission")
first_sheet.write(0, 3, "agent contribution")

for index, entry in enumerate(agent_names):
    first_sheet.write(index + 1, 0, entry)

for index, entry in enumerate(agent_sales):
    first_sheet.write(index + 1, 1, entry)

for index, entry in enumerate(agent_commission):
    first_sheet.write(index + 1, 2, entry)

for index, entry in enumerate(agent_contribution):
    first_sheet.write(index + 1, 3, entry)


# WRITTING INTO THE SECOND SHEET 
second_sheet.write(0, 0, "total revenue")
second_sheet.write(0, 1, "total commission")
second_sheet.write(0, 2, "net revenue")

second_sheet.write(1, 0, total_revenue)
second_sheet.write(1, 1, total_commission)
second_sheet.write(1, 2, net_revenue)

  
book.save("C:/users/denra/Documents/python/raveurbans.xls")
book.save(TF())

