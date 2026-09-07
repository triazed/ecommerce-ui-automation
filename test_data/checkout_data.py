from test_data.registration_data import new_user


def new_user_checkout_data():
    user = new_user()
    return {
        "email": user["email"],
        "password": user["password"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "country_name": "Australia",
        "state_name": "Queensland",
        "city_name": "Toowoomba",
        "address_1": "Carlton House 3 Mill Street",
        "zip_code": "4350",
        "phone_number": "+61234567890"
    }

def existing_user_checkout_data():
    return {
        "country_name": "Serbia",
        "state_name": "Serbia",
        "city_name": "Belgrade",
        "address_1": "Makedonska, 19",
        "zip_code": "11233",
        "phone_number": "+88234567890"
    }
