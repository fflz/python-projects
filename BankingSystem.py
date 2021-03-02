import random

class Account:
    def __init__(self, card, pin, balance):
        self.card = card
        self.pin = pin
        self.balance = balance
    def generate_pin():
        pin = random.randint(1000, 9999)
        return pin
    def create_account(self):
        firstdigits = 400000
        lastdigits = random.randint(1000000000, 9999999999)
        self.card = str(firstdigits) + str(lastdigits)
        self.pin = Account.generate_pin()
        return self.card
    def log_account(self):
        return
accounts = {
}
def main_menu():
    choose = -1;
    while (choose != 0):
            print("1. Create an account\n2. Log into account\n0. Exit")
            choose = int(input())
            if (choose == 1):
                new = Account(0,0,0)
                Account.create_account(new)
                accounts[new.card] = new.pin
                print("Your card number:\n" + str(new.card))
                print("Your card PIN:\n" + str(new.pin))
            elif (choose == 2):
                print("Enter your card number:")
                account_card = str(input())
                print("Enter your PIN:")
                account_pin = int(input())

                if ((account_card in accounts) and (account_pin in accounts.values())):
                    print("You have successfully logged in!")
                    choose2 = -1
                    while (choose2 != 0):
                        print("1. Balance\n2. Log out\n0. Exit")
                        choose2 = int(input())
                        if (choose2 == 1):
                            print("Balance: " + str(new.balance))
                        elif (choose2 == 2):
                            print ("You have successfully logged out!")
                            main_menu()
                        elif (choose2 == 0):
                            print("Bye!")
                            exit()
                else:
                    print("Wrong card number or PIN!")
            elif (choose == 0):
                exit()
                    
main_menu()
