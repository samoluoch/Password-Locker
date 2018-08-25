import unittest
from credential_data import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):

        self.new_credential = Credential("samsoluoch", "password", "twitter")
        