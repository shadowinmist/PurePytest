# This is a sample Python script.
from typing import SupportsIndex


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Person:
    def __init__(self,name=None,age=None, roles=None, bits =None):
        self.name = name
        self.age = age
        self.roles = roles if roles else set()
        self.bits = bits if bits else 0

    def __repr__(self):
        return f'{self.name} is {self.age} years old and have {self.roles} role'

    def has_role(self, check_role):
        return True if check_role in self.roles else False

    def __contains__(self, item):
        return True if item in self.roles else False

    def has_bits(self, check_bits):
        return True if self.bits & check_bits else False

    def __or__(self, other):
        return Person(bits=(self.bits | other.bits))

    def __and__(self, other):
        return Person(bits=(self.bits & other.bits))

    def show(self):
         return bin(self.bits)

    def grant(self, bit_granted):
        self.bits |= bit_granted
        # bitowe OR na masce

    def revoke(self, bit_revoked):
        self.bits &= ~bit_revoked

    def getMask(self):
        return self.bits

#
# p = Person(name="Marcin", age=30)
# p.grant(1)   # READ
# p.grant(2)   # WRITE
# print(p.getMask())        # 3
# print(p.has_bits(1))      # True  (READ jest)
# print(p.has_bits(4))      # False (EXECUTE nie ma)
# p.revoke(1)               # usuwamy READ
# print(p.getMask())        # 2
# print(p.show())           # 0b10

#
# a = Person("michal", "22",roles=["a","b","c"], bits=0b01001)
# b = Person("michal", "22",roles=["a","b","c"], bits=0b01101)
# print(a.show())
# print(b.show())
#
# c = a | b
# d = a & b
#
# print(c.show())
# print(d.show())
#

# a = Person('A',20, 'admin')
# print(repr(a))
# print(a.has_role('admin'))
# a.has_role('manager')
