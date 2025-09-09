### Tanya Kadiyala
### CMSY-257-300
### Lab 2
### Problem 2: Bank Class

class BankAccount:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0.0
        self.__transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transactions.append(('Deposit', amount))
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.__balance -= amount
        self.__transactions.append(('Withdrawal', amount))
    
    def get_balance(self):
        return self.__balance
    
    def statement(self):
        statement_lines = []
        statement_lines.append(f"Statement for {self.__owner}")
        statement_lines.append("-" * 30)
        
        for trans_type, amount in self.__transactions:
            statement_lines.append(f"{trans_type}: ${amount:.2f}")
        
        statement_lines.append("-" * 30)
        statement_lines.append(f"Final Balance: ${self.__balance:.2f}")
        
        return "\n".join(statement_lines)
    
    def __str__(self):
        return f"Account owner: {self.__owner}, Balance: ${self.__balance:.2f}"


# Driver code
if __name__ == "__main__":
    # Create an account
    acct = BankAccount("Tanya Kadiyala")
    
    # Perform deposits
    acct.deposit(100)
    acct.deposit(50)
    acct.deposit(25)
    
    # Perform withdrawals
    acct.withdraw(60)
    
    # Attempt invalid withdrawal (should raise ValueError)
    try:
        acct.withdraw(200)  # should raise ValueError
    except ValueError as e:
        print("Error:", e)
    
    # Print the account and the statement
    print(acct)
    print()
    print(acct.statement())