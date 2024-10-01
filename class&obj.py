class Car:
    # Constructor to initialize attributes
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method to display car details
    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")


car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.display_info()  # Output: Brand: Toyota, Color: Red
car2.display_info()  # Output: Brand: Honda, Color: Blue

car1.color = "Black"  # Changing the color
car1.display_info()  # Output: Brand: Toyota, Color: Black


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0  # Initial speed

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

    def accelerate(self, increment):
        self.speed += increment
        print(f"The car is now going at {self.speed} km/h")

car1 = Car("Toyota", "Red")
car1.accelerate(30)  # Output: The car is now going at 30 km/h
