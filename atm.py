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
        print("3. CHECK BALANCE \t\t4. CHANGE PIN\n5. QUICKTELLER\t\t\t6. EXIT")

        op = int(input("\n"))
        system('cls')

        if op == 1:
            amount = int(input("Enter amount: "))
            self.deposit(amount)

        elif op == 2:
            amount = int(input("Enter amount: "))
            self.withdrawal(amount)

        elif op == 3:
            return self.main_balance

        elif op == 4:
            old_pin = int(input("Enter your old pin: "))
            if self.pin == old_pin:
                new_pin = int(input("Enter your new pin"))
            else:
                print("Incorrect pin")
                
        elif op == 5:
            ch2 = int(input("1. RECHARGE\t2. PAYBILL"))
            if ch2 == 1:
                ph = input("Enter your phone number: ")
                am = int(input("Enter amount: "))
                if am < self.main_balance:
                    print("Recharge successful")
                    self.main_balance -= am
                else:
                    print("insufficient Balance!")
                self.perf_ope()
             
        elif ch2 == 2:
            am = int(input(
            "You want to pay your bill, enter the amount"
            ))
            print("payment successfull!")
            if am < self.main_balance:
                print("Recharge successful")
                self.main_balance -= am
            self.perf_ope()
        elif op == 6:
            print(
                "Thanks for banking with us, ur convinience is our concern"
            )
        else:
            print("Invalid input")

    def deposit(self, amount):
        if amount > 0:
            self.main_balance += amount
            print("Deposit successful")
            print("\n Main account balance is: ", self.main_balance)

    def withdrawal(self, amount):
        if amount < self.main_balance:
            self.main_balance -= amount
            print("Take your cash")
            print("Your main balance is: ", self.main_balance)
            self.perf_ope()
            
        else:
            print("Insufficient balance")
            self.perf_ope()
            
    def perf_ope(self):
	    ch = input("Do you want to perform another operation? 'y/n' ")
	    if ch == 'y':
		    self.show_dash()
	    else:
		    self.exit()
			


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
