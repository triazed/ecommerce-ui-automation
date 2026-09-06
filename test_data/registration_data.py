import pytest
from utils.reg_data_generator import (
    generate_email,
    generate_password,
    generate_last_name,
    generate_first_name
)
from test_data import expectations


def new_user():
    email = generate_email()
    password = generate_password()
    confirm_password = password
    first_name = generate_first_name()
    last_name = generate_last_name()
    return {
        "email": email,
        "password": password,
        "confirm_password": confirm_password,
        "first_name": first_name,
        "last_name": last_name,
    }

invalid_email_data = [
    pytest.param(
        "",
        expectations.EMPTY_REG_EMAIL_FIELD,
        id="EMPTY_EMAIL_FIELD"
    ),
    pytest.param(
        "test",
        expectations.INVALID_REG_EMAIL_ADDRESS,
        id="INVALID_EMAIL_ADDRESS"
    ),
]

invalid_password_data = [
    pytest.param(
        "12345",
        expectations.INCORRECT_REG_PASSWORD,
        id="PASSWORD_LESS_THAN_6_CHARACTERS"
    ),
    pytest.param(
        "01234567890123456789012345678901234567890123456789012345678901234",
        expectations.INCORRECT_REG_PASSWORD,
        id="PASSWORD_GREATER_THAN_64_CHARACTERS"
    ),
]


