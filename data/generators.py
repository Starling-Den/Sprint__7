from faker import Faker


fake = Faker()

def login_generator():
    login_gen = fake.user_name()
    return login_gen

def password_generator():
    password_gen = fake.user_name()
    return password_gen

def name_generator():
    name_gen = fake.user_name()
    return name_gen
