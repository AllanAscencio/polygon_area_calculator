class Rectangle:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return ((f"*" * self.width) + "\n") * self.height

    def get_amount_inside(self, ob):
        return self.get_area() // ob.get_area()

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, width: int,):
        super().__init__(width, height=width)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, width=0, height=0):
        self.width = width
        self.height = width

    def set_width(self, width):
        self.set_side(width)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())
#
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))

rect.set_width(51)
rect.set_height(3)
print(rect.get_picture())