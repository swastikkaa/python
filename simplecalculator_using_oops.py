class calculator:
   def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2

   def add(self):
     return num1+num2
   
   def square(self):
    return num1**2 
   
   def divide(self):
    return num1/num2
   
   def multiply(self):
    return num1*num2
   
   def subtract(self):
    return num1-num2
  
while True:
   num1=float(input("enter first number:"))
   num2=float(input("enter second number:"))
   operation=input("enter operation (square/divide/multiply/subtract/add):")
   a=calculator(num1,num2)
   if(operation=="square"):
    print("square of first number is:",a.square())
   if(operation=="divide"):
    print("division gives:",a.divide())
   if(operation=="multiply"):
    print("multiplication gives:",a.multiply())
   if(operation=="subtract"):
    print("subtraction gives:",a.subtract()) 
  
   answer=input("do you want to continue(yes/no)?")
   if(answer=="no"):
    break
   
