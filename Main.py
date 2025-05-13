class Vehicle:
    def __init__(self, capacity, fare_per_seat):
        self.capacity = capacity
        self.fare_per_seat = fare_per_seat

class Bus(Vehicle):
    def __init__(self, capacity, fare_per_seat):
        super().__init__(capacity, fare_per_seat)

    def calculate_fare(self, num_passengers):
        total_fare = self.fare_per_seat * num_passengers * 1.10
        return total_fare

bus = Bus(50, 100)
fare = bus.calculate_fare(50)
print("Total fare: INR", fare)