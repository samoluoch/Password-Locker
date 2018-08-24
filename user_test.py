import unittest
from user_data import User

class TestUser(unittest.TestCase):
    def setUp(self):

        self.new_user = User("samsoluoch", "wordpass")
    
    def test_init(self):
        self.assertEqual(self.new_user.username, "samsoluoch")
        self.assertEqual(self.new_user.password, "wordpass")