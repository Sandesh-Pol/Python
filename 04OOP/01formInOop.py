class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f'{self.brand} car with model {self.model}'


class ElectricCar(Car):
    def __init__(self,brand,model,charge):
        super().__init__(brand,model)
        self.charge = charge


tesala = ElectricCar("Tesala","Model S","85KWH")

print((tesala.fullName()))




# car = Car("Toyota","Corolla")

# print(car.fullName())


