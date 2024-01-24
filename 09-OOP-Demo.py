class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius")
        return self._radius

  
    @property
    def area(self):
        print("Getting area")
        return 3.14 * self._radius ** 2

my_circle = Circle(radius=5)

print("Radius:", my_circle.radius)
print("Area:", my_circle.area)
