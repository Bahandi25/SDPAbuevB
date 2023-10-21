class Car:
    def accelerate(self):
        pass

class LeMansCar:
    def lemans_engine_on(self):
        print("24 hours starts now!")

class F1Car:
    def f1_engine_on(self):
        print("And it's lights out, and away we go!")

class LeMansAdapter(Car):
    def __init__(self, lemans_car):
        self.lemans_car = lemans_car

    def accelerate(self):
        self.lemans_car.lemans_engine_on()

class F1Adapter(Car):
    def __init__(self, f1_car):
        self.f1_car = f1_car

    def accelerate(self):
        self.f1_car.f1_engine_on()

def operate_car(car):
    car.accelerate()

if __name__ == "__main__":
    lemans_car = LeMansCar()
    lemans_adapter = LeMansAdapter(lemans_car)

    f1_car = F1Car()
    f1_adapter = F1Adapter(f1_car)

    operate_car(lemans_adapter)
    operate_car(f1_adapter)