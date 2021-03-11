import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()


def is_odd(number):
    if (number % 2) != 0:
        return True
    else:
        return False


def generate_pin():
    pin = random.randint(1000, 9999)
    return pin


class Account:
    def __init__(self, card, pin, balance):
        self.card = card
        self.pin = pin
        self.balance = balance

    def create_account(self):
        firstdigits = 400000
        lastdigits = random.randint(100000000, 999999999)
        self.card = str(firstdigits) + str(lastdigits)
        carditerable = list(map(int, self.card))
        checksum = 0
        for i in range(1, 16):
            if is_odd(i):
                carditerable[i - 1] = int(carditerable[i - 1]) * 2
            if carditerable[i - 1] > 9:
                carditerable[i - 1] = carditerable[i - 1] - 9
            checksum += carditerable[i - 1]
        finaldigit = (checksum * 9) % 10
        self.card = str(firstdigits) + str(lastdigits) + str(finaldigit)
        self.pin = generate_pin()
        cur.execute("INSERT INTO card(number, pin) VALUES(?, ?)", (self.card, self.pin))
        conn.commit()
        return self.card


accounts = {
}


def checkbalance(accountcard):
    cur.execute("SELECT balance FROM card WHERE number = (?)", [accountcard])
    return cur.fetchone()[0]


def add_income(accountcard, income):
    cur.execute("UPDATE card SET balance = (balance + ?) WHERE number = (?)", (income, accountcard))
    conn.commit()


def checkluhn(transfercard):
    carditerable = list(map(int, transfercard))
    checksum = 0
    for i in range(1, 16):
        if is_odd(i):
            carditerable[i - 1] = int(carditerable[i - 1]) * 2
        if carditerable[i - 1] > 9:
            carditerable[i - 1] = carditerable[i - 1] - 9
        checksum += carditerable[i - 1]
    finaldigit = (checksum * 9) % 10
    if finaldigit == carditerable[15]:
        return True
    else:
        return False


def maketransfer(accountcard, transfercard, transferquantity):
    cur.execute("UPDATE card SET balance = (balance - ?) WHERE number = (?)", (transferquantity, accountcard))
    conn.commit()
    cur.execute("UPDATE card SET balance = (balance + ?) WHERE number = (?)", (transferquantity, transfercard))
    conn.commit()


def closeaccount(account_card):
    cur.execute("DELETE FROM card WHERE number = (?)", [account_card])
    conn.commit()


def main_menu():
    choose = -1
    while choose != 0:
        print("1. Create an account\n2. Log into account\n0. Exit")
        choose = int(input())
        if choose == 1:
            new = Account(0, 0, 0)
            Account.create_account(new)
            accounts[new.card] = new.pin
            print("Your card number:\n" + str(new.card))
            print("Your card PIN:\n" + str(new.pin))
        elif choose == 2:
            print("Enter your card number:")
            account_card = str(input())
            print("Enter your PIN:")
            account_pin = int(input())

            if (account_card in accounts) and (account_pin in accounts.values()):
                print("You have successfully logged in!")
                choose2 = -1
                while choose2 != 0:
                    print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log Out\n0. Exit")
                    choose2 = int(input())
                    if choose2 == 1:
                        print("Balance: " + checkbalance(str(account_card)))
                    elif choose2 == 2:
                        income = input("Enter income:")
                        add_income(account_card, income)
                        print("Income was added!")
                    elif choose2 == 3:
                        transfercard = input("Transfer")
                        if not checkluhn(transfercard):
                            print("Probably you made a mistake in the card number. Please try again!")
                        if not (transfercard in accounts):
                            print("Such a card does not exist.")
                        else:
                            transferquantity = int(input("Enter how much money you want to transfer:"))
                            if transferquantity > checkbalance(str(account_card)):
                                print("Not enough money!")
                            else:
                                maketransfer(account_card, transfercard, transferquantity)
                                print("Sucess!")
                    elif choose2 == 4:
                        closeaccount(account_card)
                    elif choose2 == 5:
                        print("You have successfully logged out!")
                        main_menu()
                    elif choose2 == 0:
                        print("Bye!")
                        exit()
            else:
                print("Wrong card number or PIN!")
        elif choose == 0:
            exit()


main_menu()
