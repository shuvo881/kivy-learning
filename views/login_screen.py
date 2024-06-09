from kivy.uix.screenmanager import Screen
from utils.database import load_data

class LoginScreen(Screen):
    def login(self, username, password):
        users = load_data('data/sample_data.json')['users']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    