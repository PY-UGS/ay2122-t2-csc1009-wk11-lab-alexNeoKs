class clockTime:
    

    def __init__(self):
        self.hours = self.minutes = self.seconds = "00"
        
        self.menu()
        
        while self.userinput:
            if self.userinput == "1":
                self.setHours()
                self.menu()
            elif self.userinput == "2":
                self.setMinutes()
                self.menu()
            elif self.userinput == "3":
                self.setSeconds()
                self.menu()
            elif self.userinput == "4":
                print(self.setTime())
                self.menu()
            elif self.userinput == "5":
                self.showTime()
                break
                
        
    def menu(self):
        
        print("Enter 1 to set hours\n")
        print("Enter 2 to set minutes\n")
        print("Enter 3 to set seconds\n")
        print("Enter 4 to set everything\n")
        print("Enter 5 to display time\n")
       
        self.userinput = input("Please enter a number: ")
        
    
    def setHours(self):
        userinput = input("Please enter hour in 24 format(example 16): ")
        self.hours = userinput
        
    def setMinutes(self):
        userinput = input("Please enter minutes in 24 format(example 32): ")
        self.minutes = userinput
        
    def setSeconds(self):
        userinput = input("Please enter seconds in 24 format(example 32): ")
        self.seconds = userinput
    
    def setTime(self):
        userinput = input("Please enter hour in 24 format(example 16): ")
        self.hours = userinput
        userinput = input("Please enter minutes in 24 format(example 32): ")
        self.minutes = userinput
        userinput = input("Please enter seconds in 24 format(example 32): ")
        self.seconds = userinput
    def showTime(self):
        print(self.hours +":"+ self.minutes +":"+ self.seconds)
        


test = clockTime()