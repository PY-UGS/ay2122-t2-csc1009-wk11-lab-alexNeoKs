import os

class calculator:
    
    def __init__(self):
        self.menu()
        
        
        
        while self.userinput:
            if self.userinput == "1":
                print(self.adder())
                self.menu()
            elif self.userinput == "2":
                print(self.subtractor())
                self.menu()
            elif self.userinput == "3":
                print(self.multiplier())
                self.menu()
            elif self.userinput == "4":
                print(self.divider())
                self.menu()
            elif self.userinput == "5":
                self.clear()
                
            
                
    
    def menu(self):
        print("Hello to the calculator: ")
        print("Enter 1 to add\n")
        print("Enter 2 to subtract\n")
        print("Enter 3 to multiply\n")
        print("Enter 4 to divide\n")
        print("Enter 5 to clear\n")
        print()
        self.userinput = input("Please enter a number: ")
        
        
    def adder(self):
        userinput1 = input("Please enter a number to add: ")
        userinput2 = input("Please enter another number to add: ")
        result = int(userinput1) + int(userinput2)
        
        return result
    
    def subtractor(self):
        userinput1 = input("Please enter a number to sub: ")
        userinput2 = input("Please enter another number to sub: ")
        result = int(userinput1) - int(userinput2)
        
        return result
    
    def multiplier(self):
        userinput1 = input("Please enter a number to mul: ")
        userinput2 = input("Please enter another number to mul: ")
        result = int(userinput1) * int(userinput2)
        
        return result
    
    def divider(self):
        userinput1 = input("Please enter a number to div: ")
        userinput2 = input("Please enter another number to div: ")
        result = int(userinput1) / int(userinput2)
        
        return result

    def clear(self):
        os.system('cls||clear')
    
test = calculator()