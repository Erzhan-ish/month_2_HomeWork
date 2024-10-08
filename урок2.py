class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_name(self):
        return self.__name

    def set_age(self,age):
        if type(age) == int and age >0:
            self.__age = age
        else:
            raise ValueError('wrong age. it must be an positive integer')

    def get_age(self):
        return self.__age

    def info(self):
        return f'Name: {self.__name}, Age: {self.__age}, Birth Year: {2024 - self.__age}'
    
    def voice(self):
        pass

class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

# some_animal = Animal('anim',3)
# some_animal.set_age(5)
# print(some_animal.info())

class Cat(Animal):
    def __init__(self, name, age):
        #super().__init__(name, age)
        super(Cat,self).__init__(name, age)

    def voice(self):
        print('Meow')

class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog,self).__init__(name, age)
        self.__commands = commands

    def info(self):
        return super().info() + f', Commands: {self.__commands}'

    def voice(self):
        print('woof')

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, commands):
        self.__commands = commands

class FightingDog(Dog):
    def __init__(self, name, age, commands,wins):
        super(FightingDog,self).__init__(name, age, commands)
        self.__wins = wins

    def voice(self):
        print('RRRR woof')
        
    def info(self):
        return super().info() + f', Wins: {self.__wins}'

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value


cat = Cat('Tom',2)
# print(cat.info())

dog = Dog('sharik', 10,'sit, run, bark')
dog.commands = 'sit, run'
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('reks',1,'fight',8)
# print(fighting_dog.info())

fish = Fish('nemo',2)

animals_list = [cat,dog,fighting_dog,fish]
for animal in animals_list:
    print(animal.info())
    animal.voice()
