class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total balance = ", self.balance)

user1 = Account(98000, 432)
user1.credit(3000)
user1.debit(2000)

#Encapsulation is using the attributes, and methods  by using the objects or creating objects.