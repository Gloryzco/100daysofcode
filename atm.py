# This program models a simple ATM operation

from os import system
from time import sleep


class ATMuser():
    def __init__(self, pin):
        self.pin = pin
        self.main_balance = 0

    def show_dash(self, pin):
        system('cls')
        print("1. DEPOSIT\t\t\t2. WITHDRAWAL")
        print(
            "3. CHECK BALANCE \t\t4. CHANGE PIN\n5. QUICKTELLER\t\t\t6. EXIT"
        )

        op = int(input("\n"))
        system('cls')

        if op == 1:
            amount = int(input("Enter amount: "))
            self.deposit(amount)

        elif op == 2:
            amount = int(input("Enter amount: "))
            self.withdrawal(amount)

        elif op == 3:
            print("your main balance is: ", self.main_balance)
            self.perf_ope()

        elif op == 4:
            oldPin = input("Enter old pin: ")
            self.changePin(oldPin)

        elif op == 5:
            ch2 = int(input("1. RECHARGE\t2. PAYBILL\n"))
            if ch2 == 1:
                input("Enter your phone number: ")
                am = int(input("Enter amount: "))
                if am < self.main_balance:
                    print("\n\tpls wait...")
                    sleep(1.7)
                    print("Recharge successful")
                    self.main_balance -= am
                    print("\n Main account balance is: ", self.main_balance)
                else:
                    print("insufficient Balance!")
                self.perf_ope()

            elif ch2 == 2:
                am = int(input(
                    "\nYou want to pay your bill, \nEnter the amount: "
                    ))
                if am < self.main_balance:
                    self.main_balance -= am
                    print("\n\tpls wait...")
                    sleep(1.7)
                    print("payment successfull!")
                    print("\n Main account balance is: ", self.main_balance)
                    self.perf_ope()
                else:
                    print("insufficient Balance!")
                self.perf_ope()
        elif op == 6:
            self.exit()
        else:
            print("Invalid input")

    def deposit(self, amount):
        if amount > 0:
            self.main_balance += amount
            print("\n\tpls wait...")
            sleep(1.7)
            print("Deposit successful")
            print("\n Main account balance is: ", self.main_balance)
            self.perf_ope()

    def changePin(self, old_pin):
        if self.pin == old_pin:
            new_pin = input("Enter new pin: ")
            c_new_pin = input("Confirm pin: ")
            if new_pin == c_new_pin:
                print("\n\tPls wait...")
                sleep(1.5)
                self.pin = new_pin
                print("Pin changed successfully")
            else:
                print("\n\tPls wait...")
                sleep(1.5)
                print("pin do not match")
        else:
            print("Incorrect pin")
        self.perf_ope()

    def withdrawal(self, amount):
        if amount < self.main_balance:
            self.main_balance -= amount
            print("\n\ttransaction in progress...")
            sleep(1.7)
            print("Take your cash")
            print("Your main balance is: ", self.main_balance)
            self.perf_ope()

        else:
            print("\n\ttransaction in progress...")
            sleep(1.7)
            print("Insufficient balance")
            self.perf_ope()

    def perf_ope(self):
        ch = input("Do you want to perform another operation? 'y/n' ")
        if ch == 'y':
            system('cls')
            pin = input("Enter your pin: ")
            if self.pin == pin:
                self.show_dash(pin)
            else:
                print("incorrect pin!")
        elif ch == 'n':
            self.exit()
        else:
            system('cls')
            print("invalid input!")
            self.perf_ope()

    def exit(self):
        system('cls')
        print("Thanks for banking with us")


print("\tWELCOME TO GMajor ATM")
pin = input("create your pin: ")
if pin.isdigit():
    if len(pin) > 5 or len(pin) < 4:
        print("pin should be four '4' digit")
    else:
        atm_user = ATMuser(pin)
        atm_user.show_dash(pin)
else:
    print("pin should be integer value")
