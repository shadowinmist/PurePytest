# tests/conftest.py
import pytest
from src.class_practice import Person

# --- Podstawowe fixtures ---

@pytest.fixture
def empty_person():
    return Person(name="Marcin", age=30, roles=["user"])

@pytest.fixture
def empty_person_with_bits():
    return Person(name="Marcin", age=30, roles=["user"], bits=0b11)

@pytest.fixture
def person_with_bits():
    p = Person(name="Alice", age=25, roles=["READ", "WRITE", "EXECUTE", "DELETE"], bits=0b1101)
    p.grant(1)  # READ
    p.grant(2)  # WRITE
    return p

@pytest.fixture
def permission_map():
    return {
        "NONE": 0,
        "READ":    1,
        "WRITE":   2,
        "EXECUTE": 4,
        "DELETE":  8
    }


@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_json_dummy():
    json_dummy = {
        'userId': 1,
        'title': "foo",
        'body': "bar",
    }
    return json_dummy

