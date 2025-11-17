class Car:
    def __init__(self, brand, model, year, speed=0.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0.0
    def drive(self, input_speed):
        self.speed = input_speed
    def stop(self):
        self.speed = 0.0

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.drive(55)
print("Car 1 speed:", car1.speed)
car2.drive(75)
print("Car 2 speed:", car2.speed)

car1.stop()
print("Car 1 speed after stopping:", car1.speed)
print("Car 2 speed remains:", car2.speed)
        