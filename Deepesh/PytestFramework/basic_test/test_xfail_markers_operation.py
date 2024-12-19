import pytest

ENV = "PROD"


@pytest.mark.smoke
def test_addition():
    num1 = 40
    num2 = 50
    assert num1 + num2 == 90


@pytest.mark.xfail
@pytest.mark.smoke
def test_multiplication():
    num1 = 50
    num2 = 5
    assert num1 * num2 == 300


@pytest.mark.smoke
def test_subtraction():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200


@pytest.mark.skipif(ENV != "TEST", reason="Feature in only available in Test")
@pytest.mark.smoke
@pytest.mark.sanity
def test_addition_fun1():
    num1 = 40
    num2 = 50
    assert num1 + num2 == 90


@pytest.mark.skip
@pytest.mark.sanity
def test_multiplication_fun2():
    num1 = 50
    num2 = 5
    assert num1 * num2 == 300


@pytest.mark.xfail
@pytest.mark.smoke
@pytest.mark.sanity
def test_subtraction_fun3():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200


@pytest.mark.regression
def test_addition_fun4():
    num1 = 40
    num2 = 50
    assert num1 + num2 == 90


@pytest.mark.regression
def test_multiplication_fun5():
    num1 = 50
    num2 = 5
    assert num1 * num2 == 300


@pytest.mark.xfail
@pytest.mark.regression
def test_subtraction_fun6():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200
