import unittest
from credential_data import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):

        self.new_credential = Credential("samsoluoch", "password", "twitter")

    def test_init(self):
        self.assertEqual(self.new_credential.username, "samsoluoch")
        self.assertEqual(self.new_credential.password, "password")
        self.assertEqual(self.new_credential.website, "twitter")

    def tearDown(self):
        '''
        tearDown() method that cleans up after every run
        '''
        Credential.credential_list = []

# test 1
#save_credential
    def test_save_credential(self):
        '''
        save_credential method for saving the new credential object by appending it to the credential_list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)


# test 2
    def test_delete_credential(self):
        '''
        delete_credential method that removes a credential object from the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("samsoluoch", "pass1", "twitter")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)


# test 3



if __name__ == '__main__':
    unittest.main()