#property()
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("get_radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("set_radius")
        if value < 0:
            raise ValueError("Значення радіусу не може бути меньше 0")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("delete_radius")
        del self._radius

    #radius = property(get_radius, set_radius, delete_radius)
    #radius = radius.getter(get_radius)

circle = Circle(10)
#print(circle.get_radius())
#circle.set_radius(100)
#print(circle.get_radius())
print(circle.radius) #fget=get_radius
radius = 100
print(circle.radius)
del circle.radius
print(circle.radius)