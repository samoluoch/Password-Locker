import unittest
from user_data import User

class TestUser(unittest.TestCase):
    def setUp(self):

        self.new_user = User("samsoluoch", "wordpass")
    
    def test_init(self):
        self.assertEqual(self.new_user.username, "samsoluoch")
        self.assertEqual(self.new_user.password, "wordpass")


    def tearDown(self):
        '''
        tearDown method for cleaning up after every test has run
        '''
        User.user_list = []
# first test
# save_user_list
    def test_save_user(self):
        '''
        save_user method that appends a new_user to the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


# second test for saving multiple users
# display users
    
    def test_save_multiple_user(self):
        '''
        save_multiple_user to test the ability to save multiple users
        '''
        self.new_user.save_user()
        test_user = User ("test", "thispassword")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


#third test
 # delete user
    def test_delete_user(self):
        '''
        delete_user method that uses the remove method from the user_list
        '''
        self.new_user.save_user()
        test_user = User ("test", "thispassword")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)






if __name__ == '__main__':
    unittest.main()