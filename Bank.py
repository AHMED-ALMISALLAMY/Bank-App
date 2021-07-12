class User:
    def __init__(self, name, age, gender) -> None:
        self.username = name
        self.age = age
        self.gender = gender


    def show_details(self):
        print("Name:", self.username)
        print("Age is:", self.age)
        print("Gender is", self.gender)


class Bank(User):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)

        self.balance = 0

    def deposit(self,amount):
        """Add money to your account"""
        self.amount = amount
        self.balance += self.amount
        print("Your balance has been update: $", self.balance)


    def with_draw(self, amount):
        """Take money from your account balance"""
        self.amount = amount

        if self.amount > self.balance:
            print(self.username ,"Insuffcient Funds | Balance Available: $", self.balance)
        else:
            self.balance -= self.amount
            print("Your balance has been updated: $", self.balance)


    def view_balance(self):
        """ View your account details and your balance """
        self.show_details()
        print("Account balance: $", self.balance)


Ahmed = Bank("Ahmed",15,"male")
Jack = Bank("Jack",24,"male")
Mohammed = Bank("Mohammad",41,"male")
Sam = Bank("Sam",44,"male")
kris = Bank("Kris",21,"male")



Ahmed.deposit(200)

Ahmed.with_draw(100)

Ahmed.view_balance()
