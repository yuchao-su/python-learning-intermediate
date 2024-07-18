
v = 'a'
print(type(v))



# __init__
# __str__


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f'Car make: {self.make}, model: {self.model}, year: {self.year}'


if __name__ == "__main__":
    car1 = Car('Toyota', 'Camry', 2022)
    car2 = Car('Ford', 'Mustang', 2019)
    print(car1)
    print(car2)