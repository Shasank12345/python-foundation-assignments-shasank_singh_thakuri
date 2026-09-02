class Vehicle:
    def __init__(self, country: str, company: str):
        self.country = country
        self.company = company

    def describe(self):
        print(f"Country: {self.country}, Company: {self.company}")


class Car(Vehicle):
    def __init__(self, country: str, company: str, mileage: str = "15 km/L"):
        super().__init__(country, company)
        self.mileage = mileage

    def describe(self):
        print(f"Country: {self.country}, Company: {self.company}, Mileage: {self.mileage}")


class SuperCar(Car):
    def __init__(self, country: str, company: str, mileage: str, turbo: bool = True):
        super().__init__(country, company, mileage)
        self.turbo: True = turbo

    def describe(self):
        print(f"Country: {self.country}, Company: {self.company}, Mileage: {self.mileage}, Turbo: {self.turbo}")




car_1 = Car(country="Japan", company="Toyota", mileage="18 km/L")
car_1.describe()

super_car_1 = SuperCar(country="Italy", company="Ferrari", mileage="6 km/L", turbo=True)
super_car_1.describe()
