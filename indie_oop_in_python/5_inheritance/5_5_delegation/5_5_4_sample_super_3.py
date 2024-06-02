class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        print("Я Хирург")


class MainSurgeon(Surgeon):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Главный Хирург")


s = MainSurgeon()
s.tell_about_yourself()