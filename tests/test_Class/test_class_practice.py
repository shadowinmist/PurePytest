from src.class_practice import Person
import pytest


def test_grant(empty_person):
    empty_person.grant(1)
    empty_person.grant(2)
    assert empty_person.getMask() == 3

def test_contain(empty_person):
    assert empty_person.__contains__("user") == True
    empty_person.grant(2)
    assert empty_person.__contains__("admin") == False


def test_revoke(person_with_bits):
    assert person_with_bits.getMask() == 15
    person_with_bits.revoke(1)
    assert person_with_bits.getMask() == 14

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
    assert person_with_bits.has_role("WHAT") == False

def test_bits_check(person_with_bits):
    assert person_with_bits.has_bits(0b1101) == True

def test_or_check(person_with_bits, empty_person_with_bits):
    assert (person_with_bits | empty_person_with_bits) == Person(bits=15)

def test_or_check_negative(person_with_bits):
    with pytest.raises(TypeError):
        person_with_bits | None

def test_and_check(person_with_bits, empty_person_with_bits):
    assert (person_with_bits & empty_person_with_bits) == Person(bits=3)

def test_and_check_negative(person_with_bits):
    with pytest.raises(TypeError):
        person_with_bits | "new_person"

def test_person_default_init():
    p = Person()
    assert p.name is None
    assert p.age is None
    assert p.bits == 0
    assert p.roles == set()


def test_eq_check_true():
    assert Person(bits=3) == Person(bits=3)


def test_eq_check_false():
    assert (Person(bits=3) == Person(bits=1)) is False


def test_eq_check_negative():
    assert (Person(bits=3) == "abc") is False



def test_revoke_not_existing_bit(empty_person):
    empty_person.revoke(4)
    assert empty_person.getMask() == 0


def test_or_check_negative(person_with_bits):
    with pytest.raises(TypeError):
        person_with_bits | "new_person"


def test_and_check_negative(person_with_bits):
    with pytest.raises(TypeError):
        person_with_bits & "new_person"


def test_contains_false(empty_person):
    assert ("admin" in empty_person) is False


def test_show_zero():
    p = Person(bits=0)
    assert p.show() == bin(0)