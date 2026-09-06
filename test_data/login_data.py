import pytest
from test_data import expectations


invalid_email_data = [
    pytest.param(
        "",
        expectations.EMPTY_EMAIL_FIELD,
        id="EMPTY_EMAIL_FIELD"
    ),
    pytest.param(
        "test",
        expectations.INVALID_EMAIL_ADDRESS,
        id="INVALID_EMAIL_ADDRESS"
    ),
]

non_existent_user_data = {
    "email": "uhdsf43w8refzbjhj@test.com",
    "password": "123@456"
}

invalid_password_data = [
    pytest.param(
        "123@456",
        expectations.INCORRECT_PASSWORD,
        id="PASSWORD_DOES_NOT_MATCH"
    ),
    pytest.param(
        "",
        expectations.INCORRECT_PASSWORD,
        id="EMPTY_PASSWORD"
    ),
]

