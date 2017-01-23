# Bank class module

from Account import Account
import random

class Bank():
    # list of accounts
    __acounts = []
    
    # new account method generates a number of account and a pin randomly
    # the numbers are big 4 digit pin and 6 digit nr account and the risk of collision is small
    def newAccount(self):
        nrAccount = random.randint(100000, 999999)
        pin  = random.randint(1000, 9999)
        print("This are your login info \nnrAccount : " + str(nrAccount) + "\npin : " + str(pin))
        self.__acounts.append(Account(0, nrAccount, pin))

    # for deleting an account the nr of account and pin are required then if the account is found in 
    # the list of account it is deleted
    def delAccount(thisself):
        nrAccount = int(input("What is the number of the account that you want to delete: "))    
        pinAccount = int(input("Pin of the account to confirm the delete: "))
        for thisaccount in thisself.__acounts:
            if thisaccount.login(nrAccount, pinAccount):
                if not thisaccount.hasMoney():
                    thisself.__acounts.remove(thisaccount)
                    print("Delete succesfully")
                else:
                    print("Cannot delete this account because it still has money")
            
    # login sesion followed by access in the user account
    def login(self, accountNumber, pin):
        if len(self.__acounts) > 0:
            found = False
            for thisaccount in self.__acounts:
                if thisaccount.login(accountNumber, pin):
                    # if all criteria are meet user has access to his account and can perform some tasks described in __operationAccount
                    self.__operationAccount(thisaccount)
                    found = True
                    break
            if found == False:
                print("There is no account at this bank with this accountNumber and pin")
        else:
            print("The bank has no account")

    def __operationAccount(thisself, thisAccount):
        # command for an account are the following:
        # - deposit
        # - withdraw
        # - raport 
        # - transfer money in between accounts
        comand = int(1)
        while comand > 0:
            comand = int(input("For deposit enter 1, for withdraw enter 2, for raport enter 3, for transfer enter 4, to log out enter 0. Your option: "))
            
            if comand == 1:
                thisAccount.deposit()
            if comand == 2:
                thisAccount.withdraw()
            if comand == 3:
                thisAccount.raport()
            
            # the transfer task
            if comand == 4:
                nrAccount = int(input("Number of account to transfer money: "))
                found = False
                for thisaccount in thisself.__acounts:
                    if thisaccount.transfer(nrAccount):
                        found = True
                        nrMoney = int(input("The sum to transfer: "))
                        # if the account is found
                        if thisAccount.withdrawMoney(nrMoney):
                            # if there are enough money in the account to transfer
                            thisaccount.depositMoney(nrMoney)
                            print("Transfer succesfully")
                       
                if found == False:
                    print("This account doesn't exist")
            