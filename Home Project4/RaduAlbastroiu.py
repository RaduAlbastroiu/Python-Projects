# Homework2 Radu Albastroiu
# Homework number: 2

from Bank import Bank

# bank init, there could be more banks but for ease will use just one
ING = Bank()

comand = 1
while comand > 0:
    # command for bank :
    # - new account
    # - login
    # - delete account
    comand = int(input("For creating a new account enter 1, for log in enter 2, for delete an account enter 3, for stop enter 0: "))
    
    if comand == 1:
        ING.newAccount()
    
    if comand == 2:
        accountNr = input("Enter your account Number: ")
        accountPin = input("Enter your account Pin: ")
        ING.login(accountNr, accountPin)

    if comand == 3:
        ING.delAccount()