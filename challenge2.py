class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1
    
       
c = Calculator(10, 94)
print("Addition is: ",c.add()) 
print("Subtraction is: ",c.subtract()) 
print("Multiplication is: ",c.multiply())
print("Division is: ",c.divide()) 


#Output:-

# 104
# 84
# 940
# 9.4

    


