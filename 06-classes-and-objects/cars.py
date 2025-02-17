
class Car:
    def __init__(self, brand, km):
        self.brand = brand
        self.km = km
        self.speed = 0

    def __str__(self):
        return self.brand + " speed: " + str(self.speed)
    
    def accelerate(self): 
        self.speed += 10

    def slowdown(self):
        if self.speed > 10:
            self.speed -= 10
        else:
            self.speed = 0


a = Car("BMW", 2000) 
b = Car("Toyota", 1200)
a.accelerate()
a.accelerate()


print(a)
print(b)