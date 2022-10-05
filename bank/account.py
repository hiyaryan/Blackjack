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
        self.bet = []
    
    def deposit(self, funds):
        '''
        From menu deposit allows 1$, $5, $10, $20, $100 bills.
        '''
        print(f"{self.name} deposited ${funds:.2f}")
        self.balance += funds

    
    def withdraw(self, funds):
        '''
        Withdraw from account to purchase tokens.
        '''

        if funds <= self.balance:
            print(f"\n{self.name} withdrew ${funds:.2f}")
            self.balance -= funds
            
            return True
            
        else:
            print(f"\n{self.name} has insufficient funds.")

            return False

    
    def add_tokens(self, opt, tokens=None):
        '''
        From menu exchange, converts cash to tokens. Adds to tokens on win.
        Options: E = Exchange, W = Win
        '''
        if opt == 'E':
            # Input number of tokens
            token_options = ["[1] ¢1", "[2] ¢5", "[3] ¢10", "[4] ¢20", "[5] ¢100", "[r] Return"]
            token_options_dict = {0: '1', 1: '5', 2: '10', 3: '20', 4: '100', 5: "Return"}

            token_menu = TerminalMenu(token_options, title="\n- Tokens -\n")
            token_selection = token_options_dict[token_menu.show()]

            total = 0
            value = 0
            while token_selection != 'Return':
                amount = None
                while not amount:
                    try:
                        amount = int(input(f"\nEnter the number of ¢{token_selection} tokens desired.\n\tAmount: "))
                    
                        if amount < 0:
                            print("\nInvalid input: Please enter a value greater than or equal to 0.\n")
                            amount = None
                            
                        else:
                            # Check the amount is greater than 0 and that enough funds were withdrawn
                            if amount > 0 and self.withdraw(int(token_selection) * amount):
                                for i in range(amount):
                                    self.tokens[token_selection].append(Token(token_selection, int(token_selection)))
                                    value += int(token_selection)

                                total += amount
                        
                    except ValueError:
                        print("\nInvalid input: Please enter a number only.\n")

                    token_selection = token_options_dict[token_menu.show()]
                    
            # Calculate tokens returned based on desired amount and dollar amount.
            if total > 0:
                print(f"\n{self.name} purchased {total}x tokens valued at ${value}.\n")
        
        elif opt == 'W':
            # Add tokens to the current bet
            self.bet.extend(tokens)

            # Add bet to account tokens.
            for token in self.bet:
                self.tokens[token.face].append(token)

            self.bet = []

    def subtract_tokens(self, opt, tokens=None):
        '''
        From menu exchange, converts tokens to cash. Subtracts from tokens on bet.
        Options: E = Exchange, B = Bet
        '''
        tokens_available = False
        for key in self.tokens:
            if len(self.tokens[key]) > 0:
                tokens_available = True

        # Subtract tokens from the account to be cashed out.
        if opt == 'E':
            print(f"{self.name} is selling tokens...")

        # Subtract tokens from the account to be bet.
        elif opt == 'B':

            # If the account is the dealer's match the bet then return.
            if self.name == "Dealer":
                self.bet = tokens
                print(f"{self.name} matches the bet.\n")
                return

            # If the account is the players and there are tokens available
            # access the Bet menu to make a bet.
            if tokens_available:
                bet = []
                value = 0
            
                print(self)

                # Options for the bet menu depend on the tokens available.
                options = []
                i = 1
                for key in self.tokens:
                    if len(self.tokens[key]) > 0:
                        options.append(f"{[i]} ¢{key} {len(self.tokens[key])}x")
                        i += 1

                options.append("[b] Bet")

                bank_menu = TerminalMenu(options, title=f"\n- {self.name}'s Bet -\n")
                selection = bank_menu.show()

                # Present the Bet menu, the last option at index len(optios)-1
                # is the Bet option.
                while selection != len(options) - 1:
                    '''
                    Bet menu item example: `[1] ¢20 5x`. Split with " " delimiter.
                        option[0] = [1]
                        option[1] = ¢20
                        option[2] = 5x
                    '''
                    amount = int(options[selection].split(' ')[2][:-1]) - 1

                    # Subtracts a token from the bank and appends it to the bet
                    if amount >= 0:
                        token_info = f"{options[selection].split(' ')[0]} {options[selection].split(' ')[1]} {amount}x"
                        options[selection] = token_info

                        token = self.tokens[options[selection].split(' ')[1][1:]].pop()
                        bet.append(token)
                        
                        value += int(options[selection].split(' ')[1][1:])
                        
                        if amount == 0:
                            options.pop(selection)
                    
                    bank_menu = TerminalMenu(options, title=f"\n- {self.name}'s Bet -\n")
                    selection = bank_menu.show()

                self.bet = bet

                if len(bet) != 0:
                    print(f"{self.name} is betting {len(bet)}x tokens valued at ${value}")
                    return True

                else:
                    print(f"{self.name} must place a bet to play.")
                    return False

            else:
                print(f"{self.name} has no tokens to bet.")
                return False
            

    def menu(self):
        '''
        Menu to navigate account.
        Options: Details, Deposit, Exchange
        '''
        options = ["[i] Details", "[d] Deposit", "[e] Exchange", "[r] Ready", "[q] Quit"]
        options_dict = {0: 'Details', 1: 'Deposit', 2: "Exchange", 3: 'Ready', 4: 'Quit'}

        bank_menu = TerminalMenu(options, title=f"\n- {self.name}'s Bank -\n")
        selection = options_dict[bank_menu.show()]

        while selection != "Ready" and selection != "Quit":
            if selection == "Details":
                print(self)
                
            elif selection == "Deposit":
                deposit_options = ["[1] $1.00", "[2] $5.00", "[3] $10.00", "[4] $20.00", "[5] $100.00", "[r] Return"]
                deposit_options_dict = {0: 1, 1: 5, 2: 10, 3: 20, 4: 100, 5: "Return"}

                deposit_menu = TerminalMenu(deposit_options, title="\n- Deposit -\n")
                deposit_selection = deposit_options_dict[deposit_menu.show()]

                if deposit_selection != "Return":
                    self.deposit(deposit_selection)
                
            elif selection == "Exchange":
                exchange_options = ["[b] Buy Tokens", "[s] Sell Tokens", "[r] Return"]
                exchange_options_dict = {0: 'Buy', 1: 'Sell', 2: "Back"}

                exchange_menu = TerminalMenu(exchange_options, title="\n- Exchange -\n")
                exchange_selection = exchange_options_dict[exchange_menu.show()]

                if exchange_selection == "Buy":
                    self.add_tokens('E')

                elif exchange_selection == "Sell":
                    self.subtract_tokens('E')
            
            selection = options_dict[bank_menu.show()]

        if selection == "Quit":
            return "Quit"
        
    
    def __str__(self):
        tokens = ""
        for t in self.tokens:
            if len(self.tokens[t]) > 0:
                tokens += (f"¢{t} {len(self.tokens[t])}x ${int(t) * len(self.tokens[t])}, ")
        
        return f"\n{self.name}'s Account\n\tBalance: ${self.balance:.2f}\n\tTokens:  {tokens[:-2]}\n"