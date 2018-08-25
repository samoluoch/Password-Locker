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
        
