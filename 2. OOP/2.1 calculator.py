class Calculator:
    brand = "Casio MS990"
    #add method
    def add(self, num1,num2):
        return num1+num2
    #deduct method
    def deduct(self,num1, num2):
        return num1-num2
    
    #multyply method
    def multiply(self,num1,num2):
        return num1*num2;

    #divide method
    def devide( self,num1,num2):
        return num1/num2
    
num1 = 100
num2 = 50

calculate = Calculator()

print(calculate.add(num1,num2))
print(calculate.deduct(num1,num2))
print(calculate.multiply(num1,num2))
print(calculate.devide(num1,num2))