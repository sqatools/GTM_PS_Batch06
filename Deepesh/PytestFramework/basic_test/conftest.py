import pytest

@pytest.fixture(scope="function", autouse=True)
def setup():
    print("\n conftest fixture initiated")
    yield
    print("\n conftest fixture completed")


@pytest.fixture(scope="function")
def setup_new():
    print("\n conftest new fixture initiated")
    yield
    print("\n conftest new fixture completed")
