# Напишите определение класса Money
class Money:

    def __init__(self, dollars, cents):
        self.total_cents = 0
        self.dollars = dollars
        self.cents = cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = dollars * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int) and 0 <= cents < 100:
            self.total_cents = self.dollars * 100 + cents
        else:
            print("Error cents")

    def __str__(self):
        return (
            f"Ваше состояние составляет {self.dollars} долларов "
            f"{self.cents} центов"
        )


# Ниже располагаются проверки для класса Money

bill = Money(101, 99)
assert isinstance(bill, Money)

print(bill)  # Ваше состояние составляет 101 долларов 99 центов
print(bill.dollars, bill.cents)  # 101 99
bill.dollars = 666
print(bill)  # Ваше состояние составляет 666 долларов 99 центов
bill.cents = 12
print(bill)  # Ваше состояние составляет 666 долларов 12 центов
assert bill.total_cents == 66612
assert list(bill.__dict__.keys()) == ["total_cents"]

ken = Money(111, 90)
assert isinstance(ken, Money)
print(ken)
ken.dollars = "hello"  # Error dollars
ken.dollars = 0
print(ken)
ken.cents = [1, 2, 3]  # Error cents
ken.cents = 100  # Error cents
ken.cents = 99
print(ken)

ken.total_cents = 102343
print(ken.dollars)
print(ken.cents)
