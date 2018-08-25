#!/usr/bin/env python3.6
from user_data import User
from credential_data import Credential

def create_user(user_name, phone_number, email):
    new_user = User(user_name, phone_number, email)
    return new_user
    

def save_user(user):
    user.save_user()
    

def delete_user(user):
    user.delete_user()


def find_by_username(username):
    return User.find_by_username(username)


def user_exists(username):
    return User.user_exist(username)


def display_user():
    return User.display_user()

def main():