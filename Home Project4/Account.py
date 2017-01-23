# Account class module

class Account():  
    
    # init method creates an account with a set amount of money, with a account Number, and a pin
    def __init__(self, sumOfMoney, accountNumber, pin):
        self.__money = sumOfMoney
        self.__accountNumber = accountNumber
        self.__pin = pin
    
    # this method check if the account number and pin are correct
    def login(self, accountNumber, pin):
        if int(accountNumber) == int(self.__accountNumber) and int(pin) == int(self.__pin):
            return True
        else:
            return False
    
    # this method check only the account number
    def transfer(self, accountNumber):
        if accountNumber == self.__accountNumber:
            return True
        else:
            return False
        
    # check if there are enough money to withdraw and then decrease the amount of money
    def withdraw(self):
        amountMoney = input("The sum to withdraw: ")
        if self.__money < int(amountMoney):
            print("Operation impossible, not enough founds")
            return False
        else:
            self.__money -= int(amountMoney)
            print("Withdraw succesfull")
            return True
    
    # this method does the same thing as the previous one but this time the amount of money is specified
    def withdrawMoney(self, amountMoney):
        if self.__money < int(amountMoney):
            print("Operation impossible, not enough founds")
            return False
        else:
            self.__money -= int(amountMoney)
            return True
    
    # adds an amount of money to the account
    def deposit(self):
        amountMoney = input("The sum to deposit: ")
        self.__money += int(amountMoney)
        print("Deposit succesfull")
    
    # this method does the same thing as the previous one but this time the amount of money is specified
    def depositMoney(self, amountMoney):
        self.__money += int(amountMoney)
    
    # print the money in account
    def raport(self):
        print("Money in this account: " + str(self.__money))
    
    # this method check if there are money in account
    # this method is used in delete account method 
    def hasMoney(self):
        if self.__money > 0:
            return True
        else:
            return False