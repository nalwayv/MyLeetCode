class Bank:
    def __init__(self, balance: list[int]):
        self.bank: dict[int, int] = {i+1: num for i, num in enumerate(balance)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account2 not in self.bank:
            return False

        if self.bank.get(account1, 0) - money >= 0:
            self.bank[account1] -= money
            self.bank[account2] += money
            return True
        
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.bank:
            self.bank[account] += money
            return True
        
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.bank.get(account, 0) - money >= 0:
            self.bank[account] -= money
            return True
        
        return False
        

def main() -> None:
    print("2043. Simple Bank System")

    bank = Bank([10, 100, 20, 50, 30])
    bank.withdraw(3, 10)        # return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                                # Account 3 has $20 - $10 = $10.
    bank.transfer(5, 1, 20)     # return true, account 5 has a balance of $30, so it is valid to transfer $20.
                                # Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
    bank.deposit(5, 20)         # return true, it is valid to deposit $20 to account 5.
                                # Account 5 has $10 + $20 = $30.
    bank.transfer(3, 4, 15)     # return false, the current balance of account 3 is $10,
                                # so it is invalid to transfer $15 from it.
    bank.withdraw(10, 50)       # return false, it is invalid because account 10 does not exist.
    

if __name__ == "__main__":
    main()