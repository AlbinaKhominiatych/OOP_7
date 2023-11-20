class MyClass:
    _x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        else:
            self._x = value

obj = MyClass()
obj.x = 10  # Виведе: 10
print(obj.x)
obj.x = -5  # Виведе: 0
print(obj.x)