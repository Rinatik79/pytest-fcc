import pytest
import source.shapes as shapes

# @pytest.fixture -- don't need after conftest.py creation
# def my_rectangle():
#     return shapes.Rectangle(10, 20)
#
# @pytest.fixture
# def weird_rectangle():
#     return shapes.Rectangle(5, 6)

def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20) -- after using @pytest.fixture don't need this line any moore
    assert my_rectangle.area() == 200

def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20) -- after using @pytest.fixture don't need this line any moore
    assert my_rectangle.perimeter() == 60

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
