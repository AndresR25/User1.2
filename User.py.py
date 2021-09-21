class User:
    def __init__(self,n,lt,ag):
        self.name=n
        self.lastname=lt
        self.age=ag
        self.amount=0

    def deposit(self, amount):
        self.amount += amount
        return self
    
    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self



Andres=User("Andres","Rodriguez",19)
Silvia=User("Silvia","Alfaro",40)
Emilce=User("Emilce","Castillo",70)

Andres.deposit(5000).deposit(10000).deposit(15000).make_withdrawl(1000).display_user_balance()


Silvia.deposit(1000).deposit(2000).make_withdrawl(500).make_withdrawl(1000).display_user_balance()

Emilce.deposit(2000).make_withdrawl(1000).make_withdrawl(500).make_withdrawl(2000).display_user_balance()

Andres.transfer_money(1000,Emilce)