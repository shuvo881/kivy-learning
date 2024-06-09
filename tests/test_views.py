import unittest
from kivy.uix.screenmanager import ScreenManager
from views.login_screen import LoginScreen

class TestLoginScreen(unittest.TestCase):
    def test_login_screen(self):
        screen = LoginScreen(name='login')
        self.assertEqual(screen.name, 'login')

if __name__ == '__main__':
    unittest.main()
