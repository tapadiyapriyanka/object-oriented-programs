# Maintain the List of CompanyShares in a Linked List So new CompanyShares can be added or removed easily. Do not use any Collection Library to implement Linked List.

data_items = []
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self,newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext

class Unordered_list:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found   = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found  = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous  = current
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())

    def display(self):
        current = self.head
        while current != None:
            data_items.append(current.getdata())
            current = current.getnext()

class stock_account():
    def __init__(self):
        self.account_details = {}
        self.mylist = Unordered_list()
        
    def buy(self, symbol, amount):
        ans = self.mylist.search(symbol)
        if ans == False:
            self.mylist.add(symbol)
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
        self.mylist.display()
        print("Report of linked list = ")
        for item in data_items:
            print("items = ",item)

    def list_company_shares(self):
        c = int(input("Enter how many companies share u have = "))
        for i in range(c):
            stock_symbol = input("Enter stock symbol = ")
            self.mylist.add(stock_symbol)
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
