import pytest

# fixture is a reusable function that can be used for each test

# scope = "function" (default) fixture is called before every test function
# scope = "module" fixture is called only once before test functions
# scope = "class" fixture is called only once before class
# scope = "session" fixture is called only once before session


#make this a fixture to execute before every test function
@pytest.fixture #optional parenthesis
def setup(scope = "module"):
    print("setup browser...")
    return "chrome"

def test_my_first_test(setup):
    print("this is my first test")
    print("Browser is: ",setup)


def test_my_second_test():
    print("this is my second test")

#-----------------------------------------------------------------------------------------
# run all tests in module
#pytest test_first_test.py
#pytest test_first_test.py -s
#pytest test_first_test.py -s -v

#Run specific tests
#pytest test_first_test.py::test_my_first_test() -s -v
#pytest test_first_test.py::test_my_second_test() -s -v

# -s shows all printed outputs live in console while test runs
# -v shows detailed execution info. pytest in verbose mode

# to show what classes look like in pytest
class TestClass:
    def test_one(self):
        print("this is my first test")

    def test_two(self):
        print("this is my first test")