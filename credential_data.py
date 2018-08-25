class Credential:
    '''
    This is a class that generates instances of usernames, passwords, and the websites
    '''
    credential_list = []
    def __init__ (self, username, password, website):
        '''
        __init__ method helps in defining credential properties
        Args:
        username: New credential username
        password: New credential password
        website: New credential website
        '''
        self.username = username
        self.password = password
        self.website = website

    def save_credential(self):
        '''
        save_credential method that saves the object credential into the credential_list
        '''
        Credential.credential_list.append(self)
