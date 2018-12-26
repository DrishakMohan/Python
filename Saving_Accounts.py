# From Lambert, Fundamentals of Python: From First Programs through Data Structures

class Saving_Accounts:
    '''Savings accounts with owner's name, PIN, and balance.'''
    
    RATE = 0.02
        
    def __init__(self, name: str, pin: str, balance: int = 0) -> None:
        '''Create SavingsAccount with given name, pin, and balance.
        '''
        self._name = name
        self._pin = pin
        self._balance = balance

    def __str__(self) -> str:
        '''Return string representation of SavingsAccount.
        '''
        return 'Name: {}\nPIN: {}\nBalance: {}'.format(self._name, self._pin, self._balance)

    def get_balance(self) -> int:
        '''Return balance of this SavingsAccount.
        '''
        return self._balance

    def get_name(self) -> str:
        '''Return name of this SavingsAccount.
        '''
        return self._name

    def get_pin(self) -> int:
        '''Return PIN of this SavingsAccount.
        '''
        return self._pin

    def deposit(self, amount: int) -> int:
        '''Deposit the given amount and return the new balance.
        '''
        self._balance += amount
        return self._balance

    def withdraw(self, amount: int) -> bool:
        '''Withdraw the given amount. Return True iff successful.
        '''
        if amount < 0 or self._balance < amount:
            return False
        self._balance -= amount
        return True

    def compute_interest(self) -> int:
        '''Compute, deposit, and return the interest.
        '''
        interest = int(self._balance * Saving_Accounts.RATE)
        self.deposit(interest)
        return interest