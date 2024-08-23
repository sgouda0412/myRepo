from collections import (
    Counter,
    ChainMap,
    defaultdict,
    deque,
    UserDict,
    UserList,
    UserString,
    namedtuple,
)
import logging
import argparse
import shutil
import subprocess
import os
import sys
import platform

from abc import ABC, abstractmethod, abstractproperty


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


class Car(object):
    count = 0

    def __init__(self, brand: str, fuel_type: str) -> None:
        self.brand = brand
        self.fuel_type = fuel_type

    def run(self):
        print(f"Volvo is running.....")

    @staticmethod
    def age(ages):
        return True if ages > 18 else False

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return cls.count


volvo = Car("Vovlo", "Diseal")
print(volvo.brand)
print(volvo.fuel_type)

print(volvo.run())

print(Car.age(21))

print(Car.increase_count())

from typing import (
    List,
    Dict,
    Sequence,
    Self,
    Set,
    Sized,
    Callable,
    Coroutine,
    Awaitable,
    Annotated,
    Any,
    Union,
    Iterable,
)

from multiprocessing import Pool, Process, Queue, freeze_support
from threading import Thread
from itertools import (
    chain,
    accumulate,
    batched,
    combinations,
    combinations_with_replacement,
    compress,
    count,
    cycle,
    dropwhile,
    filterfalse,
    takewhile,
    tee,
)


from collections.abc import (
    Generator,
    Iterable,
    AsyncGenerator,
    Iterable,
    Callable,
    Hashable,
    Container,
)


# Python 3 program to find
# factorial of given number
def factorial(n):

    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 12
print("Factorial of", num, "is", factorial(num))
