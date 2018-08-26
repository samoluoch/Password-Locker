import unittest
from user_data import User

class TestUser(unittest.TestCase):
    def setUp(self):

        self.new_user = User("samsoluoch", "0726", "sam@gmail.com")
    
    def test_init(self):
        self.assertEqual(self.new_user.username, "samsoluoch")
        self.assertEqual(self.new_user.phone, "0726")
        self.assertEqual(self.new_user.email, "sam@gmail.com")


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
        test_user = User ("test", "0726", "sam@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


#third test
 # delete user
    def test_delete_user(self):
        '''
        delete_user method that uses the remove method from the user_list
        '''
        self.new_user.save_user()
        test_user = User ("test", "0726", "sam@gmail.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

#fourth test
# finding user by username
    def test_find_user_by_username(self):
        '''
        test to check if it is possible to find users by usernames and display the usernames
        '''
        self.new_user.save_user()
        test_user = User("test", "0726", "sam@gmail.com")
        test_user.save_user()

        found_user = User.find_by_username("test")

        self.assertEqual(found_user.username, test_user.username)


#fifth test
#testing a user's object existence
    def test_user_exists(self):
        '''
        method that tests if a user exists in the user_list
        '''

        self.new_user.save_user()
        test_user = User("test", "0726", "sam@gmail.com")
        test_user.save_user()

        user_exists = User.user_exist("test")

        self.assertTrue(user_exists)


# sixth test
# receiving a list of users
    def test_display_all_users(self):
        '''
        method that displays the list of users
        '''
        self.assertEqual(User.display_user(), User.user_list)




if __name__ == '__main__':
    unittest.main()