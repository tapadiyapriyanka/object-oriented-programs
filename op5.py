# Commercial data processing

class stock_account():
    def __init__(self):
        self.account_details = {}
        
    def buy(self, symbol, amount):
        if symbol not in self.account_details[symbol]:
            self.account_details[symbol] = amount
        else:
            original_amount = self.account_details[symbol]
            if original_amount > amount:
                new_amount = original_amount + amount
                self.account_details[symbol] = new_amount
            else:
                print("there are not that much shares to buy. ")
            
        
    def sell(self, symbol, amount):
        original_amount = self.account_details[symbol]
        if original_amount > amount:
            new_amount = original_amount - amount
            self.account_details[symbol] = new_amount
        else:
            print("there are not that much shares to sell. ")

    def print_report(self):
        print("detailed report of stocks = ",self.account_details)

    def list_company_shares(self):
        c = int(input("Enter how many companies share u have = "))
        for i in range(c):
            stock_symbol = input("Enter stock symbol = ")
            no_shares = int(input("Enter shares of company = "))
            self.account_details[stock_symbol] = no_shares

s = stock_account()
s.list_company_shares()
b_sym = input("Enter which symbol you want to buy = ")
b_amt = int(input("Enter how many shares you want to buy = "))
s.buy(b_sym, b_amt)

s_sym = input("Enter which symbol you want to sell = ")
s_amt = int(input("Enter how many shares you want to sell = "))
s.sell(s_sym, s_amt)

s.print_report()
