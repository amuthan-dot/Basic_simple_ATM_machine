

class Customer:
    bank = "State Bank of India"
    def __init__(self, name, balance=0.00):

        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Balance after deposit : ",self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("You have insufficient balance")
            exit()
        else:
            self.balance -= amount
            print("Balance after Withraw : ",self.balance)

name = input("Enter Your name : ")
print("Hi ",name,"! Welcome to ",Customer.bank)
c = Customer(name)

while True:

    print(" D - Deposit \t W - Withdraw \t E - Exit " )
    option = input("Enter Ur Option : ")

    if option == 'd' or option == 'D':
        amount = float(input(" Enter the Deposit Amount : "))
        c.deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input(" Enter the Withraw amount : "))
        c.withdraw(amount)
    elif option == 'e' or option == 'E':
        exit()
    else:
        print("You Entered a Invalid Option")
        

    
