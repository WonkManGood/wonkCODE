class Jar:
    def __init__(self, size):
        self.capacity = 12
        self.size = size

    def __str__(self):
        return str('🍪' * self.size)

    def deposit(self, n):
        if n + self.size >=

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > 12:
            return ValueError("Too many cookies!!!")
        self._size = size

print(Jar(1))