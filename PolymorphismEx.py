class Car:
    def start(self):
        return 'the car starts'

class Bicycle:
    def start(self):
        return 'the bicycle starts' 

class Bus:
    def start(self):
        return 'the bus starts'

def start_transport(transport):
    print(transport.start())
    
my_car = Car()
my_bicycle = Bicycle()
my_bus = Bus() 

start_transport(my_car) 
start_transport(my_bicycle)
start_transport(my_bus)