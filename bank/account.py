# Account
from simple_term_menu import TerminalMenu
from bank.token import Token

class Account:
    def __init__(self, name):
        '''
        name: same as player role in Hand class.
        balance: monetary balance in account.
        tokens: dict of tokens, e.g. '5': 10 == 10 $5 Tokens
        '''
        
        self.name = name
        self.balance = 0
        self.tokens = {'1': [], '5': [], '10': [], '20': [], '100': []}
    
    def deposit(self, funds):
        '''
        From menu deposit allows 1$, $5, $10, $20, $100 bills.
        '''
        print(f"{self.name} deposited ${funds:.2f}")
        self.balance += funds

    def add_tokens(self, opt, sum=0):
        '''
        From menu exchange, converts cash to tokens. Adds to tokens on win.
        Options: E = Exchange, W = Win
        '''
        if opt == 'E':

            # Input dollar amount.
            # value = None
            # while not value:
            #     try:
            #         value = int(input("\nEnter a full dollar amount.\n\tValue: $"))

            #         if value <= 0:
            #             print("\nInvalid input: Please enter a value greater than 0.\n")
            #             value = None
                
            #     except ValueError:
            #         print("\nInvalid input: Please enter a number only.\n")

            # Input number of tokens
            token_options = ["[1] 1", "[2] 5", "[3] 10", "[4] 20", "[5] 100", "[d] Done"]
            token_options_dict = {0: '1', 1: '5', 2: '10', 3: '20', 4: '100', 5: "Done"}

            token_menu = TerminalMenu(token_options, title="\n- Tokens -\n")
            token_selection = token_options_dict[token_menu.show()]

            total = 0
            value = 0
            while token_selection != 'Done':
                amount = None
                while not amount:
                    try:
                        amount = int(input(f"\nEnter the number of ¢{token_selection} tokens desired.\n\tAmount: "))
                    
                        if amount < 0:
                            print("\nInvalid input: Please enter a value greater than or equal to 0.\n")
                            amount = None
                            
                        else:
                            if amount > 0:
                                for i in range(amount):
                                    self.tokens[token_selection].append(Token(token_selection, int(token_selection)))
                                    value += int(token_selection)

                                total += amount
                        
                    except ValueError:
                        print("\nInvalid input: Please enter a number only.\n")

                    token_selection = token_options_dict[token_menu.show()]
                    
            # Calculate tokens returned based on desired amount and dollar amount.
            print(f"\n{self.name} purchased ¢{total} tokens valued at ${value}.")
        
        elif opt == 'W':
            pass

    def subtract_tokens(self, opt, diff=0):
        '''
        From menu exchange, converts tokens to cash. Subtracts from tokens on lose.
        Options: E = Exchange, L = Lose
        '''
        if opt == 'E':
            print(f"{self.name} is selling tokens...")
        
        elif opt == 'L':
            pass

    def menu(self):
        '''
        Menu to navigate account.
        Options: Details, Deposit, Exchange
        '''
        options = ["[i] Details", "[d] Deposit", "[e] Exchange", "[b] Back"]
        options_dict = {0: 'Details', 1: 'Deposit', 2: "Exchange", 3: 'Back'}

        bank_menu = TerminalMenu(options, title=f"\n- {self.name}'s Bank -\n")
        selection = options_dict[bank_menu.show()]

        while selection != "Back":
            if selection == "Details":
                print(self)
                
            elif selection == "Deposit":
                deposit_options = ["[1] $1.00", "[2] $5.00", "[3] $10.00", "[4] $20.00", "[5] $100.00", "[b] Back"]
                deposit_options_dict = {0: 1, 1: 5, 2: 10, 3: 20, 4: 100, 5: "Back"}

                deposit_menu = TerminalMenu(deposit_options, title="\n- Deposit -\n")
                deposit_selection = deposit_options_dict[deposit_menu.show()]

                if deposit_selection != "Back":
                    self.deposit(deposit_selection)
                
            elif selection == "Exchange":
                exchange_options = ["[p] Buy Tokens", "[s] Sell Tokens", "[b] Back"]
                exchange_options_dict = {0: 'Buy', 1: 'Sell', 2: "Back"}

                exchange_menu = TerminalMenu(exchange_options, title="\n- Exchange -\n")
                exchange_selection = exchange_options_dict[exchange_menu.show()]

                if exchange_selection == "Buy":
                    self.add_tokens('E')

                elif exchange_selection == "Sell":
                    self.subtract_tokens('E')
            
            selection = options_dict[bank_menu.show()]
        
    
    def __str__(self):
        return f"\n{self.name}'s Account\n\tBalance: ${self.balance:.2f}\n\tTokens:  {self.tokens}\n"