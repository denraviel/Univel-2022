class EthnicMeal:
    def igbo(self):                                           
        print("Akpu")
    
    def yoruba(self):
        print("Amala")

    def hausa(self):
        print("Tuwo shinkafa")


meal_one = EthnicMeal()
# meal_one.hausa()

# class Student:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def get_name(self):                  #accessor instance method
#         return self.name
    
#     def get_gender(self):
#         return self.gender
    
#     def get_age(self):
#         return self.age
    
#     def set_name(self, Value):           #mutator instance method
#         self.name = Value
#     def set_gender(self, Value):
#         self.gender = Value
#     def set_age (self,Value ):
#         self.age = Value



# stu_one = Student("Harvey", "Male", 22)
# stu_two = Student("Bridget", "Female", 27)
# stu_three = Student("Jerry", "Male", 25)


# # print(stu_one.get_name())

# # print(stu_two.get_age())

# # stu_two.set_age(23)
# # print(stu_two.get_age())


# class School:
#     no_of_students = 0
#     sum_of_scvores = 0
    
#     def __init__(self, student_name, Student_score):
#         self.student_name = student_name
#         self.student_score = Student_score
#         School.increase_count()
#         School.sum_of_scvores += self.get_student_score()

#     def get_student_name(self):
#         return self.student_name

#     def get_student_score(self):
#         return self.student_score

#     def set_students_name(self,dip):
#         self.student_name = dip

#     def set_student_score(self,dip):
#         self.student_score = dip


#     @classmethod
#     def increase_count(cls):
#         cls.no_of_students += 1

#     @classmethod
#     def average_scores(cls):
#         output = cls.sum_of_scvores / cls.no_of_students
#         return round(output,2)
    
        
        
        

    
# edu_one = School("Pepe", 55.7)
# # edu_one.increase_count()
# edu_two = School("Odegaard", 89.20)
# # edu_two.increase_count()
# # print(School.no_of_students)

# print(School.average_scores())

# Instance_collector = [School("Ifeoma",64.22), School("Kepa", 45.87), School("Lukaku", 34.6)] 
# print(Instance_collector[1].get_student_score())
import csv

class Personal_info():
    def __init__(self, name, gender, age, location):
        self.name = name
        self.gender = gender
        self.age = age
        self.location = location
        Personal_info.writes(self)
        Personal_info.checks(self)
        
        
    def writes(self):
        user_file = open("C:/users/denra/Documents/univiel city class/used.csv",mode= "a",encoding= "utf-8", newline="")
        pen = csv.writer(user_file)
        pen.writerow([self.name, self.gender,self.age,self.location])
    

    def gett_name(self):
        return self.name

    def gett_gender(self):
        return self.gender

    def gett_age(self):
        return self.location
    
    def set_name(self,value):
        self.name = value

    def set_gender(self, value):
        self.gender = value

    def set_age(self,value):
        self.age = value
    
    def set_location(self,value):
        self.location = value
    
    def checks(self):
        Personal_inn = input("Re-enter name here: ")
        Personal_in_age = input("Re- enter age: ")
        user_file = open("C:/users/denra/Documents/python/used.csv", mode= "r")
        read_the_file = user_file.readlines()
        d_strip = [entry.rstrip("\n") for entry in read_the_file]
    
        # for x in d_strip:
        #     if Personal_inn == x[0] and Personal_in_age == x[2]:
                

Personal_in =Personal_info(input("input name :"), input("gender :"), input("age :"), input("location :"))






    


