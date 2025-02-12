class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model
        # self.total_car+=1
        Car.total_car+=1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} : {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        print("Car is very good")
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery=battery

    def fuel_type(self):
        return "Electricity"

# my_tesla=ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.full_name())

# print(my_tesla.__brand)
# print(my_tesla.get_brand())

mycar=Car("Tata", "Nexon")
# print(mycar.brand)
# print(mycar.model)
# print(mycar.full_name())

# print(Car.total_car)
# print(mycar.total_car)
