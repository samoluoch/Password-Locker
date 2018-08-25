#!/usr/bin/env python3.6
from user_data import User
from credential_data import Credential

def create_user(user_name, phone_number, email):
    new_user = User(user_name, phone_number, email)
    return new_user


