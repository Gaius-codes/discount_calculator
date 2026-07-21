class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        line = '*' * self.width + '\n'
        return line * self.height

    def get_amount_inside(self, square):
        horizontal_fit = self.width // square.width
        vertical_fit = self.height // square.height

        return horizontal_fit * vertical_fit

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

square = Square(5)
print(square.get_area())

