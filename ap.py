class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


rec = Rectangle(20,10)

print(str(rec), repr(rec))









