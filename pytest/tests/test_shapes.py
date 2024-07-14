import pytest
import math
import time
import source.shapes as shapes

# @pytest.mark.usefixtures("setup")
# class TestCircle():

#     def setup_method(self, method):
#         print(f"set up the class {method}")
#         # self.circle = shapes.Circle(10)

#     def teardown_method(self, method):
#         print(f"Tearing down from the class {method}")
    
#     def test_one(self):
#         print("Testing the area of the circle")
#         # assert self.circle.area() == math.pi * self.circle.radius ** 2

#     def test_two(self):
#         print("Actual Test happening here")
#         assert True


def test_crossBrowser(crossbrowse, setup):
    print("This is where I actually running the test",crossbrowse[1])


@pytest.fixture
def weird_rectangle():
    print("I am being passed as second")
    rect = shapes.Rectangle(10, 20)
    rect1 = shapes.Rectangle(10, 20)
    rect2 = shapes.Rectangle(10, 20)
    yield rect
    print("Now I am cleaning up the 2nd items")

# Ordering of passing this fixuture matter since, they
# Will be excecuted in a particular order
def test_rectangle_not_equal(my_rectangle,weird_rectangle):
    # Basically this test is aiming to match the 2 rectangle objects
    print("Now after first and thrid, I am running")
    assert my_rectangle == weird_rectangle
    print("cleaning up myself")


@pytest.mark.parametrize("side_length, expected_area",[(10,100),(11,121)])
def test_multiple_square_areas(side_length,expected_area,my_rectangle):
    print("Testing square areas")
    time.sleep(5)
    assert shapes.Square(side_length).area() == expected_area