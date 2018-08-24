class User:
    '''
    This is a class that generates new instances of usernames and password
    '''
    user_list = []
    def __init__ (self, username, password):
        '''
        __init__ methods that helps in defining the object properties
        Args:
        username: New user username
        password: New user password
        '''

        self.username = username
        self.password = password

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


