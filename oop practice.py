# class HumanKind: #class creation

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

# human_kind_object = HumanKind() # object craetion or class instantiation
# print(human_kind_object)

# print(human_kind_object.skin)

# object = []
# for i in range(8):
#     object.append(HumanKind())
# print(object)
import winsound
import time
# class HumanKind: #class creation

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"
#     def describe(self):
#         print(f"hello  my species is {self.species}")
#     def makenoise(self):
#         print("hello !!!")
#         winsound.Beep(700,500)
#         time.sleep(1)
#         winsound.Beep(700, 500)
#         time.sleep(1)
#         winsound.Beep(700, 500)
# varname = HumanKind()
# varname.describe()
# varname.makenoise()

# class Cat:
#     name = "Zed"
#     fur_colour = "Brown"
#     Family = "felidae"
#     def description(self):
#         print(f" hello i am a cat, my fur colour is {self.fur_colour}, and my name is {self.name}, I am from {self.Family} family. ")
# sand = Cat()
# sand.description()

#INSTANCE ATTRIBUTES
import random
import winsound

class Person:

    species = "Homo Sapiens"
    _class  = "Maammal"

    def __init__(self,name, complexion, height):
        self.name = name
        self.complexion = complexion
        self.height = height
        self.voice_freq = random.randint(700, 550)
    def say_something(self):
        print(f"Hello, my name is {self.name}.\n I am {self._class}, and my height is {self.height}")
        winsound.Beep(self.voice_freq,20000)
        time.sleep(0.5)
        winsound.Beep(self.voice_freq, 1800)
        time.sleep(0.5)
        winsound.Beep(self.voice_freq, 5000)
person1 = Person(name="Ade", complexion= "Brown skin", height= "5ft7")
person1.say_something()

person2 = Person(name= "Segun", complexion= "Fair skin", height= "6 ft2")
person2.say_something()
  