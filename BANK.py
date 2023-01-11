class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Deposit must be positive, otherwise invalid transaction')

    def charge(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
            else:
                raise ValueError('Insufficient money in account')
        else:
            raise ValueError('Negative charge is invalid')

    def __repr__(self):
        return f'Acount[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def __repr__(self):
        return f'Bank[{self.customer_list}, {self.account_list}]'

bank = Bank()
c1 = bank.create_customer('John', 'Brown')
c2 = bank.create_customer('Anne', 'Smith')
c3 = bank.create_customer('Max', 'Miller')
print('---------------------------')
print(c1)
a1 = bank.create_account(c1)
print(a1)
a2 = bank.create_account(c1)
print(a2)
print('---------------------------')
a3 = bank.create_account(c2)
a4 = bank.create_account(c2)
print(bank)

print('-----------------------------')

print(a1)
a1.deposit(10055)
print(a1)
a1.charge(589)
print(a1)
print('------------------------------------')

a_from = bank.find_account(1001)
print('account from')
print(a_from)

a_from = bank.find_account(1003)
print('account from')
print(a_from)
print('------------------------------------')
bank.transfer(1001, 1002, 200)
print('After transfer')
print(bank)
