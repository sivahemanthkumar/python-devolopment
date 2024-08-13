class ATM:
    def __init__(self):
        self.pin = 1111
        self.balance = 100000.0
        self.scanner = input

    def pin_validation(self):
        epin = int(self.scanner("Enter Your Pin: "))
        if epin == self.pin:
            self.details()
        else:
            print("Enter A Valid Pin!")
            self.pin_validation()

    def details(self):
        print("Choose Your Options:")
        print("1. Balance Enquiry")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. PIN Change")
        print("5. Clear")

        n = int(self.scanner())
        if n == 1:
            self.balance_enquiry()
        elif n == 2:
            self.withdraw()
        elif n == 3:
            self.deposit()
        elif n == 4:
            self.change_pin()
        elif n == 5:
            self.terminate()
        else:
            print("Invalid Option")
            self.details()

    def balance_enquiry(self):
        print(f"Current Balance: {self.balance}")

    def withdraw(self):
        wit = float(self.scanner("Enter Your Withdrawable Amount: "))
        if wit <= self.balance:
            self.balance -= wit
            print("Withdraw Successful")
            print(f"Current Balance: {self.balance}")
        else:
            print("The Withdrawable Amount Cannot Exceed Your Current Balance")
            self.withdraw()

    def deposit(self):
        dep = float(self.scanner("Enter The Amount To Be Deposited: "))
        self.balance += dep
        print("Money Deposited Successfully")
        print(f"Current Balance: {self.balance}")

    def change_pin(self):
        avpin = int(self.scanner("Enter Your Current Pin: "))
        if avpin == self.pin:
            npin = int(self.scanner("Enter Your New Pin: "))
            self.pin = npin
            print(f"Pin Changed Successfully To: {npin}")
        else:
            print("Your Pin Does Not Match The Current Pin")
            self.change_pin()

    def terminate(self):
        print("Transaction Terminated")


if __name__ == "__main__":
    atm = ATM()
    atm.pin_validation()
