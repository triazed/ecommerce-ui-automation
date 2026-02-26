from utils.reg_data_generator import (
    generate_email,
    generate_password,
    generate_last_name,
    generate_first_name
)

def new_user():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "first_name": generate_first_name(),
        "last_name": generate_last_name(),
    }
