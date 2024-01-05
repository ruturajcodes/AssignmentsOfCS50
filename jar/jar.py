class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪" * self.size)


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Capacity exceeded")

        available = self.capacity - self.size



        if n <= available:
            self._size = self.size + n
        else:
            raise ValueError("Capacity exceeded")



    def withdraw(self, n):
        if n <= self.capacity and self.size > 0:
            self._size = self.size - n
        else:
            raise ValueError("Either removal quantity greater than size or jar already empty")


    @property
    def capacity(self):
        return self._capacity

    '''
    @capacity.setter
    def capacity(self, value):
        value = 12
        self._capacity = value
    '''
    
    @property
    def size(self):
        return self._size

    '''
    # @size.setter
    # def size(self, value):
    #     self._size = value
    '''

'''
def main():
    jar = Jar()
    print(jar)
    jar.deposit(10)
    print("Capacity: ",jar.capacity)
    print("Current cookie count: ", jar.size)
    jar.withdraw(7)
    print("After withdrawing 7")
    print("Current cookie count: ", jar.size)
    #
    print(jar)
    # jar.withdraw(9)
    # print(jar)
    # print("After depositing 2")
    # print("Current cookie count: ", jar.size())
    # print("Cookie count:",jar)

if __name__ == "__main__":
    main()
'''