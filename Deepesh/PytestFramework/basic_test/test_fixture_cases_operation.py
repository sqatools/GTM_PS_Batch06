import pytest
"""
Fixture is the function that we want execution  before and after execution of each cases or test suite
Fixture has following scope:

function : function level fixture executes along with each function
module : Module level fixture execute with test file level
package : Package level fixture will execute with package initiation which contains multiple modules.
session : Session level fixture will execution along with automation initiation and after completion of
          automation execution.
class : class level fixture will work will each class execution.

"""
@pytest.fixture(scope="function")
def setup():
    print("\n initiate the test case")
    yield
    print("\n test execution completed")


@pytest.fixture(scope="module", autouse=True)
def module_setup():
    print("\n module execution initiated")
    yield
    print("\n module execution completed")


@pytest.fixture(scope="package", autouse=True)
def package_setup():
    print("\n package execution initiated")
    yield
    print("\n package execution completed")

@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n session execution initiated")
    yield
    print("\n session execution completed")

def test_addition(setup):
    num1 = 40
    num2 = 50
    assert num1 + num2 == 90


def test_multiplication(setup):
    num1 = 50
    num2 = 5
    assert num1 * num2 == 300


def test_subtraction(setup):
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200
