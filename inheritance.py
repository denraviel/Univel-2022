class Staff:
    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def status (self):
        print("I am a registered staff")

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age

class Manager(Staff):
    def __init__(self,name,gender,age ,department, level):
        super().__init__(name,gender,age)
        self.department = department
        self.level = level

    def get_department(self):
        return self.department

    def get_level(self):
        return self.level

    def role_dist(self):
        print("i distribute roles")

m_one = Manager("kenderick", "male", 45, "I.T" , 5)
m_one.role_dist()
m_one.status()
print(m_one.get_name())
print(m_one.get_age())
print(m_one.get_gender())
print(m_one.get_department())
print(m_one.get_level())





