import pytest
import source.shapes as shapes

@pytest.fixture 
def my_rectangle():
    print("I am being passed as first - From the conftest level")
    rect = shapes.Rectangle(10,20)
    yield rect
    print("cleaning up 1st")

@pytest.fixture(scope="class")
def setup():
    print("I am being passed as first  - set-up from the conftest level ")
    yield
    print("cleaning up 1st  - tear-down from the conftest level")

# This fixture is calling test for 3 times with different environment
# @pytest.fixture(params=["chrome","Firefox","IE"])
@pytest.fixture(params=[("chrome","two"),("Firefox","three"),("IE","four")])
def crossbrowse(request):
    return request.param