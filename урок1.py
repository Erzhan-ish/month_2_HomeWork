class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        print(f'{self.model} changed color to {new_color}')
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)
        
    
class Car(Transport):
    counter = 0
    # constructor                 #parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # fields / attributes
        super().__init__(the_model, the_year , the_color)
        self.penalties = penalties
        Car.counter += 1
    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def signal(self, number_of_times, sound):
        while number_of_times > 0:
            print(f'Car {self.model} is signalling {sound}')
            number_of_times -= 1

class truck(Car):
    counter = 0
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year , the_color, penalties)
        self.load_capacity = load_capacity
        truck.counter += 1

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You can load more than of {product_type} ({weight} kg)')
        else:
            print(f'You successfully loaded the cargo of {product_type} ({weight} kg)')
print('start')
print(f'Factory CAR produced: {Car.counter}')
number = 65
bmw_car = Car('BMW X7', 2020, 'red')
print(bmw_car)
print(f'Model: {bmw_car.model} Year: {bmw_car.year}'
      f' Color: {bmw_car.color} Penalties: {bmw_car.penalties}')


honda_car = Car('Honda fit', 2009, 'blue', 5000  )
print(f'Model: {honda_car.model} Year: {honda_car.year} Color: '
      f'{honda_car.color} Penalties: {honda_car.penalties}')
#honda_car.color = 'Yellow'
honda_car.change_color('yellow')
print(f'Model: {honda_car.model} Year: {honda_car.year} New Color: '
      f'{honda_car.color} Penalties: {honda_car.penalties}')

mers_car = Car(penalties=400,the_model='Mercedes 120'
               ,the_year= 2017,the_color= 'silver')
print(f'Model: {mers_car.model} Year: {mers_car.year} Color: '
      f'{mers_car.color} Penalties: {mers_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Kant')

mers_car.signal(5,'Beep')
print(f'Factory CAR produced: {Car.counter}')

boening_plane = Plane('Boening 747', 2022, 'white')
print(f'Model: {boening_plane.model} Year: {boening_plane.year} Color: {boening_plane.color}')


daf_truck = truck('Daf 105', 2000, 'green', 900, 20000)
print(f'Model: {daf_truck.model} Year: {daf_truck.year} Color: {daf_truck.color}'
      f' Penalties: {daf_truck.penalties} Load Capacity: {daf_truck.load_capacity}')
daf_truck.load_cargo(product_type='potatos',weight=25000)
daf_truck.load_cargo(15000,'tomatos')
daf_truck.drive('tokmok')
print(truck.counter)
print('end')






