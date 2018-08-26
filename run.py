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
    print("Welcome to Password Locker. Please enter your username to proceed")
    user_name = input()

    print(f"Thank you {user_name}. Use the following options to proceed:")
    print('\n')

    while True:
        print("Enter code cu to create a new user, du to display users, fu to find users, and ex to exit")

        code = input().lower()

        if code == 'cu':
            print("New user")
            print("-"*10)

            print("Username...")
            user_name = input()

            print("Phone number...")
            phone_number = input()

            print("User email...")
            email = input()

            save_user(create_user(user_name, phone_number, email))
            print('\n')
            print(f"New User {user_name} {phone_number} {email} created")
            print('\n')

        elif code == 'du':
            if display_user():
                print("This is the list of available users")
                print('\n')
                for user in user_list():
                     print(f"{user.user_name} {user.phone_number} {user.email}")

                     print('\n')

            else:
                print('\n')
                print("Currently, you have no users in your list")
                print('\n')

        elif code == 'fu':
                print("Enter the username you want to such")
                user_name = input()
                if find_by_username(user_name):
                     search_username = find_by_username(user_name)
                     print(f"{search_username.user_name} {search_username.phone_number} {search_username.email}")
                     print('-'*20)

                     print(f"phone number....{search_username.phone_number}")
                     print(f"email.....{search_username.email}")

                else:
                    print("Thay user is not in your lis")

        elif code == 'ex':
                print("Have a nice time")