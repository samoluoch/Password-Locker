import pyperclip
class User:
    '''
    This is a class that generates new instances of user details
    '''
    user_list = []
    def __init__ (self, username, phone, email):
        '''
        __init__ methods that helps in defining the object properties
        Args:
        username: New user username
        phone: New user phone
        email: New user email
        '''

        self.username = username
        self.phone = phone
        self.email = email

    def save_user(self):
        '''
        save_user_list method that saves objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method that deletes a user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return username

    @classmethod
    def user_exist(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return True

        return False

    @classmethod
    def display_user(cls):
        return cls.user_list

    @classmethod
    def copy_email(cls, username):
        user_found = User.find_by_username(username)
        pyperclicp.copy(user_found.username)



