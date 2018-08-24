import unittest
from user_data import User

class TestUser(unittest.TestCase):
    def setUp(self):

        self.new_user = User("samsoluoch", "wordpass")
    
    def test_init(self):
        self.assertEqual(self.new_user.username, "samsoluoch")
        self.assertEqual(self.new_user.password, "wordpass")

# first test
# save_user_list
    def save_user_list(self):
        self.new_user.save_user_list()
        self.assertEqual(len(User.user_list), 1)







if __name__ == '__main__':
    unittest.main()