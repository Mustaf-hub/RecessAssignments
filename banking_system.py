from dataclasses import dataclass


@dataclass
class Account:
	owner: str
	balance: float

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return False
		self.balance -= amount
		return True


class Transaction:
	def __init__(self, amount):
		self.amount = amount

	def validate_amount(self):
		if self.amount <= 0:
			raise ValueError("Amount must be greater than zero.")

	def execute(self, *args):
		raise NotImplementedError("Subclasses must implement execute().")


class Deposit(Transaction):
	def execute(self, account):
		self.validate_amount()
		account.deposit(self.amount)
		return f"Deposit successful: {account.owner} received {self.amount:.2f}."


class Withdrawal(Transaction):
	def execute(self, account):
		self.validate_amount()
		if not account.withdraw(self.amount):
			return f"Withdrawal failed: {account.owner} has insufficient funds."
		return f"Withdrawal successful: {account.owner} withdrew {self.amount:.2f}."


class Transfer(Transaction):
	def execute(self, source_account, target_account):
		self.validate_amount()
		if not source_account.withdraw(self.amount):
			return (
				f"Transfer failed: {source_account.owner} has insufficient funds to send "
				f"{self.amount:.2f}."
			)
		target_account.deposit(self.amount)
		return (
			f"Transfer successful: {source_account.owner} sent {self.amount:.2f} "
			f"to {target_account.owner}."
		)


class BankingSystem:
	def process_transaction(self, transaction_type, *args):
		if transaction_type == "deposit" and len(args) == 2:
			account, amount = args
			return Deposit(amount).execute(account)

		if transaction_type == "withdrawal" and len(args) == 2:
			account, amount = args
			return Withdrawal(amount).execute(account)

		if transaction_type == "transfer" and len(args) == 3:
			source_account, target_account, amount = args
			return Transfer(amount).execute(source_account, target_account)

		raise ValueError("Invalid transaction.")


def show_balance(account):
	print(f"{account.owner} balance: {account.balance:.2f}")


def demo_banking_system():
	print("=== Banking System Demo ===")

	employer_account = Account("Employer", 1000.00)
	employee_account = Account("Employee", 250.00)
	banking_system = BankingSystem()

	print("\nInitial balances:")
	show_balance(employer_account)
	show_balance(employee_account)

	print("\n1. Employer makes a deposit")
	print(banking_system.process_transaction("deposit", employer_account, 500.00))
	show_balance(employer_account)

	print("\n2. Employer makes a withdrawal")
	print(banking_system.process_transaction("withdrawal", employer_account, 200.00))
	show_balance(employer_account)

	print("\n3. Employer transfers funds to Employee")
	print(banking_system.process_transaction("transfer", employer_account, employee_account, 300.00))
	show_balance(employer_account)
	show_balance(employee_account)


if __name__ == "__main__":
	demo_banking_system()