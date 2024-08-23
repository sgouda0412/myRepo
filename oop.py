from abc import ABC, abstractmethod
from collections import Counter
from itertools import accumulate, pairwise, tee
from collections import UserDict
from collections import defaultdict

s = Counter([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5])
print(s)


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class Truck(Vehicle):
    def move(self):
        print("Moving .....")

    def drive(self):
        print("Driving ......")


tractor = Truck()
tractor.move()
tractor.drive()
