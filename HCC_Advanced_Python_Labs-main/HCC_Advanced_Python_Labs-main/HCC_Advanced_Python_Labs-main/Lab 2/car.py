### Tanya Kadiyala
### CMSY-257-300
### Lab 2
### Problem 1: Car Class

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed = max(0, self.__speed - 5)
    
    def reset_speed(self):
        self.__speed = 0
    
    def get_speed(self):
        return self.__speed
    
    def __str__(self):
        return f"{self.__year_model} {self.__make} @ {self.__speed} mph"


# Driver code
if __name__ == "__main__":
    car = Car(2020, 'Toyota')
    
    # Accelerate 5 times and print speed each time
    print("Accelerating:")
    for i in range(5):
        car.accelerate()
        print(car.get_speed())
    
    # Brake 5 times and print speed each time
    print("\nBraking:")
    for i in range(5):
        car.brake()
        print(car.get_speed())
    
    # Reset speed and print final state
    car.reset_speed()
    print(f"\nFinal state: {car}")