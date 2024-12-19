def test_addition(setup_new):
    num1 = 40
    num2 = 50
    assert num1 + num2 == 90


def test_multiplication(setup_new):
    num1 = 50
    num2 = 5
    assert num1 * num2 == 300


def test_subtraction():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200
