from car import Sedan, SUV, Roadster

class CarFactory:
    def create_car(self, car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        elif car_type == "roadster":
            return Roadster()
        else:
            raise ValueError("Invalid car type")