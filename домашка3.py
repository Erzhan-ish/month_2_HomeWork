class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __str__(self):
        return f'CPU: {self.__cpu}, MEMORY: {self.__memory}'

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f'sim_cards_list: {self.__sim_cards_list}'

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    @staticmethod
    def call(sim_cards_number, call_to_number):
        return (f"Идет звонок на номер: {call_to_number}"
                f" с сим-карты-{sim_cards_number} - Beeline")


class Smartphone(Computer,Phone):
    def __init__(self, sim_cards_list,cpu, memory):
        Computer.__init__(self,cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def __str__(self):
        return super().__str__() + f', sim_cards_list: {self.sim_cards_list}'

    @staticmethod
    def use_gps(location):
        return f'Внимание! До {location} осталось 450 метров'

MyComputer = Computer(64,1000)
MyPhone = Phone('Beeline')
smartphone_1 = Smartphone(memory=64,cpu=8,sim_cards_list='O!')
smartphone_2 = Smartphone(memory=156,cpu=16,sim_cards_list='MegaCom')

print(MyComputer)
print(MyPhone)
print(smartphone_1)
print(smartphone_2)

print(MyComputer.make_computations())

print(MyComputer.memory > smartphone_2.memory)
print(smartphone_1.memory != smartphone_2.memory)
print(smartphone_1.memory == MyComputer.memory)
print(smartphone_1.memory < MyComputer.memory)
print(MyComputer.memory >= smartphone_1.memory)
print(smartphone_2.memory <= smartphone_1.memory)

print(MyPhone.call(2,'+996227105520'))
print(smartphone_1.call(1,'+996520160720'))

print(smartphone_1.use_gps('Филармония'))
print(smartphone_2.use_gps('Vefa'))