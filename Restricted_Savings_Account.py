# From Lambert, Fundamentals of Python: From First Programs through Data Structures

from bank import Saving_Accounts

class Restricted_Savings_Account(Saving_Accounts):
    '''Restricted savings accounts.'''

    MAX_WITHDRAWALS = 3
        
    def __init__(self, name: str, pin: str, balance: int = 0) -> None:
        '''Create RestrictedSavingsAccount with given name, pin, and balance.
        '''
        Saving_Accounts.__init__(self, name, pin, balance)
        self._counter = 0

    def withdraw(self, amount: int) -> bool:
        '''Withdraw the given amount. Return True iff successful.
        '''
        if self._counter == \
           Restricted_Savings_Account.MAX_WITHDRAWALS:
            return False
        else:
            result = Saving_Accounts.withdraw(self, amount)
            if result:
                self._counter += 1
            return result

    def reset_counter(self) -> None:
        '''Reset the number of withdrawals.
        '''
        self._counter = 0