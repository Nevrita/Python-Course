class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def display_details(self):
        print("Breed: " + self.breed + ", Color: " + self.color)

dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Bulldog", "White")
dog3 = Dog("Beagle", "Tricolor")

dog1.display_details()
dog2.display_details()
dog3.display_details()