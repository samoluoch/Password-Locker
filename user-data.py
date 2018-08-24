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

    def save_user_list(self):
        '''
        save_user_data method that saves objects into user_list
        '''
        user.user_list.append(self)
