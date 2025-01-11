# Clase para representar una cuenta bancaria
class BankAccount:
    def __init__(self, owner, balance=0):
        """
        Inicializa una cuenta con un propietario y un saldo inicial.
        :param owner: Propietario de la cuenta.
        :param balance: Saldo inicial (por defecto es 0).
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposita dinero en la cuenta."""
        self.balance += amount
        print(f"Se depositaron ${amount}. Saldo actual: ${self.balance}")

    def withdraw(self, amount):
        """Retira dinero si hay suficiente saldo."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Se retiraron ${amount}. Saldo actual: ${self.balance}")
        else:
            print("Fondos insuficientes.")


# Crear una cuenta bancaria
account = BankAccount("Luis", 100)

# Realizar operaciones
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
