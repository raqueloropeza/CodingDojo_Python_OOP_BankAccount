class BankAccount: 
    #Create a Bank Account class with two attributes.
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
    #Create a deposit method that increases the account's balance by the specified amount.
    def deposit(self, amount):
        self.balance += amount
        return 

    #Create a withdrawal method that decreases the account's balance by the specificed amount. 
    def withdrawal(self, amount):
        #Include a condition that if the balance goes below 0 to charge a $5 fee. 
        if (self.balance - amount) < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount +5)
        else:
            self.balance -= amount
        return self
    #Create a display method that prints the account's balance. 
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    #Create a yield interest method that increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
account1 = BankAccount(0.01, 200) 
account2 = BankAccount(0.2, 500)

account1.deposit(200).deposit(100).withdrawal(20).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdrawal(25).withdrawal(75).withdrawal(100).withdrawal(150).yield_interest().display_account_info()
