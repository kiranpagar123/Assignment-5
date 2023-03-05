class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

s = Student()
s.setName("kiran pagar")
s.setRollNumber("DS160123")
print(s.getName()) 
print(s.getRollNumber()) 


##Output:-

# kiran pagar
# DS160123
