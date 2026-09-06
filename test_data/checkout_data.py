from test_data.registration_data import new_user


def checkout_data():
    return {
        "email": new_user()["email"],
        "password": new_user()["password"],
        "first_name": new_user()["first_name"],
        "last_name": new_user()["last_name"],
        "country_name":"Australia",
        "state_name":"Queensland",
        "city_name":"Toowoomba",
        "address_1":"Carlton House 3 Mill Street",
        "zip_code":"4350",
        "phone_number":" +61234567890"
    }
