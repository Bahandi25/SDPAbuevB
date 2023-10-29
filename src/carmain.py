from carfactory import CarFactory
from carobserver import CarReadyEvent

def main():
    car_factory = CarFactory()

    sedan = car_factory.create_car("sedan")
    suv = car_factory.create_car("suv")
    roadster = car_factory.create_car("roadster")

    print(f"Baurzhan is {sedan.drive()}")
    
    print(f"Arsen is {suv.drive()}")
    
    print(f"Oraz is {roadster.drive()}") 
if __name__ == "__main__":
    main()