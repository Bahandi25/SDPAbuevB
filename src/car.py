class Car:
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        return "Driving a Sedan"

class SUV(Car):
    def drive(self):
        return "Driving an SUV"

class Roadster(Car):
    def drive(self):
        return "Driving a Roadster"