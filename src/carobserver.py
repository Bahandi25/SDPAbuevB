class Event:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)
 
class CarReadyEvent(Event):
    pass

class CarObserver:
    def update(self, message):
        pass

class CarDealer(CarObserver):
    def update(self, message):
        print(f"Dealer received notification: {message}")