
from user_data import User
from credential_data import Credential

def create_user(username, phone, email):
    new_user = User(username, phone, email)
    return new_user


def create_credential(username, password, website):
    new_credential = Credential(username, password, website)
    return new_credential


def save_credential(credential):
    credential.save_credential()
    

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
    username = input()


    print(f'Thank you {username} Please use the following options to proceed')
    print('\n')

    while True:
        print("Enter code cu to create a new user, du to display users, fu to find users, cc to create new credential and ex to exit")

        code = input().lower()

        if code == 'cu':
            print("New user")
            print("-"*10)

            print("Username...")
            username = input()

            print("Phone number...")
            phone = input()

            print("User email...")
            email = input()

            save_user(create_user(username, phone, email))
            print('\n')
            print(f"New User {username} {phone} {email} created")
            print('\n')


        elif code == 'cc':
            print("New credential")
            print("-"*10)

            print("Username...")
            username = input()

            print("Password...")
            password = input()

            print("Website...")
            website = input()


            save_credential(create_credential(username, password, website))
            print('\n')
            print(f"New username {username} and password {password} for application {website} created")
            print('\n')


        elif code == 'du':
            if display_user():
                print("This is the list of available users")
                print('\n')

                for user in user_list():
                     print(f"{user.username} {user.phone} {user.email}")

                     print('\n')

            else:
                print('\n')
                print("Currently, you have no users in your list")
                print('\n')

        elif code == 'fu':
                print("Enter the username you want to such")
                user_name = input()
                if find_by_username(user_name):
                     search_username = find_by_username(username)
                     print(f"{search_username.username} {search_username.phone} {search_username.email}")
                     print('-'*20)

                     print(f"phone number....{search_username.phone}")
                     print(f"email.....{search_username.email}")

                else:
                    print("Thay user is not in your list")

        elif code == 'ex':
                print("Have a nice time")

if __name__ == '__main__':
    main()