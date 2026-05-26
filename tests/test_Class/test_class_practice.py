# This is a sample Python script.
from src.class_practice import Person
import pytest
from tests.conftest import permission_map

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test_grant(empty_person):
    empty_person.grant(1)
    empty_person.grant(2)
    assert empty_person.getMask() == 3

def test_revoke(person_with_bits):
    person_with_bits.revoke(1)
    assert person_with_bits.getMask() == 2

def test_show():
    a = Person(name="Marcin", age=30, bits=1)
    assert a.show() == bin(0b01)


def test_map(empty_person,permission_map):
    assert empty_person.bits == permission_map["NONE"]


@pytest.mark.parametrize("permission", [0,1,2,3,4,5,6,7,8,9,10,12,15,2221,412312])
def test_permision(empty_person, permission:int):
    empty_person.grant(permission)
    assert empty_person.getMask() == permission

def test_repr(person_with_bits):
    assert "Alice" in repr(person_with_bits)

def test_roles_check(person_with_bits):
    assert person_with_bits.has_role("READ") == True
    assert person_with_bits.has_role("NONE") == False

# class Person:
#     def __init__(self,name=None,age=None, roles=None, bits: SupportsIndex =None):
#         self.name = name
#         self.age = age
#         self.roles = roles if roles else set()
#         self.bits = bits if bits else 0
#
#     def __repr__(self):
#         return f'{self.name} is {self.age} years old and have {self.role} role'
#
#     def has_role(self, check_role):
#         return True if check_role == self.role else False
#
#     def __contains__(self, item):
#         return True if item in self.role else False
#
#     def has_bits(self, check_bits):
#         return True if self.bits & check_bits else False
#
#     def __or__(self, other):
#         return Person(bits=(self.bits | other.bits))
#
#     def __and__(self, other):
#         return Person(bits=(self.bits & other.bits))
#
#     def show(self):
#          return bin(self.bits)
#
#     def grant(self, bit_granted):
#         self.bits |= bit_granted
#         # bitowe OR na masce
#
#     def revoke(self, bit_revoked):
#         self.bits &= ~bit_revoked
#
#     def getMask(self):
#         return self.bits
#
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
