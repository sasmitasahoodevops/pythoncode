'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1*p2)

# Output: (3,5)
'''
def num(a,b):
    sum=a+b
    return sum
n=num(4,7)
print(n)
