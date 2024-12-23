import pytest
from data_file_fac import *

@pytest.mark.parametrize("username, password", [('user1', 'pass1'), ('user2', 'pass2'), ('user3', 'pass3')])
def test_login(username, password):
    print("Username  :", username)
    print("Password :", password)


@pytest.mark.parametrize("user, password", face_user_list)
def test_facebook_login(user, password):
    print("Username  :", user)
    print("Password :", password)

#command to run python -m pytest -v -s .\test_parameterisation.py
