from kivy.uix.screenmanager import Screen

class ProfileScreen(Screen):
    def on_enter(self, *args):
        user_info = "User: john_doe\nEmail: john@example.com"  # Mock data
        self.ids.profile_label.text = user_info
