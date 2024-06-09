import unittest
from models.user_model import UserModel

class TestUserModel(unittest.TestCase):
    def test_user_creation(self):
        user = UserModel('john_doe', 'john@example.com', 'password123')
        self.assertEqual(user.username, 'john_doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.password, 'password123')

if __name__ == '__main__':
    unittest.main()
