class Jar:
    def __init__(self, size=0):
        self.capacity = 12
        self.size = size

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


J = Jar
print(J.capacity)