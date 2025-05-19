class Car:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def display_info(self):
        print("Fuel Type:", self.fuel_type)
        print("Max Speed:", self.max_speed, "km/h")

class BMW(Car):
    def __init__(self, fuel_type, max_speed):
        super().__init__(fuel_type, max_speed)

    def task(self):
        print("Car: BMW")
        self.display_info()

    def print(self, value):
        print("Value:", value)

class Ferrari(Car):
    def __init__(self, fuel_type, max_speed):
        super().__init__(fuel_type, max_speed)

    def task(self):
        print("Car: Ferrari")
        self.display_info()

    def print(self, value):
        print("Value:", value)

obj_bmw = BMW("Petrol", 250)
obj_ferrari = Ferrari("Petrol", 330)

obj_bmw.task()
obj_bmw.print(100)

print()

obj_ferrari.task()
obj_ferrari.print(100)

print()