class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.1416 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.1416 * self.radius

radius = float(input("Enter the radius: "))
circle = Circle(radius)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())