class Car:
    def __init__(self, make, model, year, color, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

    def drive(self):
        if self.current_speed > 0:
            print(f"This {self.make} {self.model} is already driving at {self.current_speed} km/h.")
        else:
            self.current_speed = 10
            print(f"This {self.make} {self.model} starts driving at {self.current_speed} km/h.")

    def accelerate(self, increase):
        if self.current_speed + increase <= self.max_speed:
            self.current_speed += increase
            print(f"This {self.make} {self.model} accelerates to {self.current_speed} km/h.")
        else:
            self.current_speed = self.max_speed
            print(f"This {self.make} {self.model} has reached its maximum speed of {self.max_speed} km/h!")

    def brake(self, decrease):
        if self.current_speed - decrease >= 0:
            self.current_speed -= decrease
            print(f"This {self.make} {self.model} slows down to {self.current_speed} km/h.")
        else:
            self.current_speed = 0
            print(f"This {self.make} {self.model} has stopped completely.")

    def stop(self):
        if self.current_speed > 0:
            print(f"This {self.make} {self.model} is stopping from {self.current_speed} km/h.")
            self.current_speed = 0
        else:
            print(f"This {self.make} {self.model} is already stopped.")

    def repaint(self, new_color):
        print(f"The {self.make} {self.model} is being repainted from {self.color} to {new_color}.")
        self.color = new_color

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model} (Max Speed: {self.max_speed} km/h)"

my_car = Car("Mercedes", "e63s", 2017, "White", 250)
print(my_car)
my_car.drive()
my_car.accelerate(50)
my_car.accelerate(150)
my_car.accelerate(60)
my_car.brake(30)
my_car.brake(200)
my_car.repaint("Red")
my_car.stop()
print(my_car)
