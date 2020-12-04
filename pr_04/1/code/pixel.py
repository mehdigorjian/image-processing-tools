import math
class Pixel:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if isinstance(other, Pixel):
            return Pixel(other.x - self.x, other.y - self.y)
        elif isinstance(other, tuple):
            return Pixel(other[0] - self.x, other[1] - self.y)
    
    def __add__(self, other):
        if isinstance(other, Pixel):
            return Pixel(other.x + self.x, other.y + self.y)
        elif isinstance(other, tuple):
            return Pixel(other[0] + self.x, other[1] + self.y)
        else:
            raise TypeError

    def __mul__(self, scalar):
        return Pixel(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f'Pixel({self.x}, {self.y})'

    def __eq__(self, other):
        return Pixel(other.x, other.y)
        
    def pix_dist_pix(self, other):
        if isinstance(other, Pixel):
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        elif isinstance(other, tuple):
            return math.sqrt((self.x - other[0])**2 + (self.y - other[1])**2)
        else:
            return TypeError