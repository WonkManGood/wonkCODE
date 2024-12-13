class Jar:
    def __init__(self, size=0, capacity=12):
        if int(size) < 0: raise ValueError('cannot have a less than zero size')
        else: self.size = int(size)
        self.capacity = capacity

    def __str__(self):
        if self._size > 0: return (f'🍪' * self.size)
        if self._size == 0: return (f'')

    def deposit(self, n):
        if self._size + n > self._capacity: raise ValueError('Inserted too many cookies!')
        else: self._size = int(self._size + n)

    def withdraw(self, n):
        if self._size - n < 0: raise ValueError('Can\'t go negative with your cookies sir!') 
        else: self._size = int(self._size - n)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if self._size > capacity:
            raise ValueError("Too many cookies!!!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size >= 12:
            raise ValueError('Too many cookies!!!')
        if size < 0: raise ValueError('Can\'t have negative cookies.')
        self._size = size