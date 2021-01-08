'''

Banking System using OOP
Parent Class  : User  --> Holds details about user ,  has a function to show show_user_details

Child class  : Bank --> Stores details about the account balance, amount, and allows fpr deposits, withdraw and veiw balance

'''
class User():
    def __init__(self,name,age,gender,phno):
        self.name=name
        self.age=age
        self.gender=gender
        self.phno=phno
    def show_details(self):
        print("Personal Details:\n")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Phone Number:",self.phno)

#Creating Child Class
class Bank(User):
    def __init__(self,name,age,gender,phno):
        super().__init__(name,age,gender,phno)
        self.balance = 0
    def deposit(self,amount):
        print('You have deposited',amount,'Sucessfully')
        self.balance = self.balance + amount
        print('Account Balance has been updated:',self.balance)
    def withdraw(self,amount):
        if self.balance >= amount:
            print("Your withdrawal amount",amount," has been successful")
            self.balance = self.balance - amount
            print("Your balance:",self.balance)
        else:
            print("You have insuffitient amount")
    def viewbalance(self):
        self.show_details()
        print("Your balance:", self.balance)





c=Bank("Ravi",19,"Male",9652792097)
c.show_details()
c.deposit(2000000000)
c.withdraw(2000)
print()
c.viewbalance()

