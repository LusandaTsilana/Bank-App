
import sys


class Bank:
    tot_customers = 0

    def __init__(self, acc_bal, name):
        pass
        self.acc_bal = acc_bal
        self.name = name
        Bank.tot_customers += 1

    def process_customer_request(self):
        self.greet()
        self.show_options()
        self.process_choices()

    def greet(self):
        print(f'Welcome to CodeBreakers Bank {self.name}!')
    
    def show_options(self):
        print('''1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit''')

    def process_choices(self):
        user_choice = int(input('Enter your choice:'))
        if user_choice == 1:
            print(f'Your account balance is: {self.acc_bal}')
        elif user_choice == 2:
            deposit_amt = int(input('Enter amount to Deposit: '))
            self.acc_bal += deposit_amt
            print(f'Your account balance is: {self.acc_bal}')
        elif user_choice == 3:
            withdraw_amt = int(input('Enter amount to Withdraw: '))
            if withdraw_amt ==0 or self.acc_bal ==0 or withdraw_amt > self.acc_bal:
                print(f'Your account balance is: {self.acc_bal} cannot perform this transaction')
                
            else:
                self.acc_bal -= withdraw_amt
                print(f'Your account balance is: {self.acc_bal}')
        elif user_choice == 4:
            print('Thank you. Visit again!!')
            sys.exit()
        else:
            print('Wrong choice. Please enter a digit that represents one of the below options.')
            print('1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit')
            sys.exit()

lusanda = Bank(13500, 'Lusanda')
lusanda.process_customer_request()
#sima = Bank(20000, 'Sima')
#sima.process_customer_request()
#mohammed = Bank(15000, 'Mohammed')
#mohammed.process_customer_request()