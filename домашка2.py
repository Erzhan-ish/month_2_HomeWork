class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self,side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        print(f'sguare side length: {self.__side_length}{Figure.unit} area: {self.calculate_area()}{Figure.unit}')

class Rectangle(Figure):
    def __init__(self,width,height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__height * self.__width

    def info(self):
        print(f'Rectangle length: {self.__height}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}')

figures = [Square(3), Square(8), Rectangle(4,9),
           Rectangle(9,2), Rectangle(13,5)]
for figure in figures:
    figure.info()
