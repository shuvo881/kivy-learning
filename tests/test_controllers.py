import unittest
from controllers.login_screen_controller import LoginScreenController

class TestLoginScreenController(unittest.TestCase):
    def test_controller_logic(self):
        controller = LoginScreenController(None)
        self.assertIsNotNone(controller)

if __name__ == '__main__':
    unittest.main()
