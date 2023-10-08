class Car:
    def price(self):
        pass
    
class CarStock(Car):
    def price(self):
        return 50000000
    
class CarOptions(Car):
    def __init__(self, car):
        self._car = car

    def price(self):
        return self._car.price()

    def priceError(self, price):
        if not self.price:
            raise ValueError("Set price!")
class MatteColor(CarOptions):
    def price(self):
        return self._car.price() + 1500000

class TurboV6Engine(CarOptions):
    def price(self):
        return self._car.price() + 3000000

if __name__ == "__main__":
    car_stock = CarStock()
    print(f"Price of Stock Car: {car_stock.price()}")
    
    car_with_options = MatteColor(TurboV6Engine(car_stock))
    print(f"Price of Car with Options: {car_with_options.price()}")