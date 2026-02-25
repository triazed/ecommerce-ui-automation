from utils import reg_data_generator

def new_user():
    return {
        'email': reg_data_generator.generate_email(),
        'password': reg_data_generator.generate_password(),
        'first_name': reg_data_generator.generate_first_name(),
        'last_name': reg_data_generator.generate_last_name(),
    }
