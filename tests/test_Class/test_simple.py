import pytest
from src.calculator import add, subtract, divide, multiply, is_even



def test_add():
    # The 'assert' keyword checks if the condition is True
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # Verify that the correct exception is raised when dividing by zero
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize("a,b,expected",[
    pytest.param(1,2,3,id="normal addition"),
    pytest.param(1000,2000,3000,id="large numbers"),
    pytest.param('c','v','s',marks=pytest.mark.xfail(reason="String math not supported yet"), id="expected failure"),

])
def test_add(a,b,expected):
    #positive test
    assert add(a, b) == expected

    #Error type test
    # with pytest.raises(TypeError):
    #     add(4,"2")


class Test_Calculator:
    def test_add(self):
        assert add(3,2)
        with pytest.raises(TypeError):
            add(4, "2")
            add("v", [0])

    def test_subtract(self):
        assert subtract(5,5) == 0

        with pytest.raises(TypeError):
            subtract(4, "2")
            subtract("v", [0])





@pytest.mark.parametrize("input_val, expected", [
    pytest.param(1, 2, id="normal addition"),
    pytest.param(99, 100, id="large numbers"),
    pytest.param("a", "b",
                 marks=pytest.mark.xfail(reason="String math not supported yet"),
                 id="expected failure")
])
def test_increment(input_val, expected):
    assert input_val + 1 == expected



@pytest.mark.parametrize("input_val, expected", [
    pytest.param(1, 1, id="normal multi"),
    pytest.param(99, 99, id="large multi"),
    pytest.param("a", "b",
                 marks=pytest.mark.xfail(reason="String math not supported yet"),
                 id="expected failure")
])
def test_multiply(input_val, expected):
    assert multiply(input_val, 1) == expected




@pytest.mark.parametrize("input_val, expected", [
    pytest.param(2, True, id="True"),
    pytest.param(99, False, id="False"),
    pytest.param("a", False,
                 marks=pytest.mark.xfail(reason="String math not supported yet"),
                 id="expected failure")
])
def test_even(input_val, expected):
    assert is_even(input_val) == expected

