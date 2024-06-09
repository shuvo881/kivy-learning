from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from views.login_screen import LoginScreen
from views.main_screen import MainScreen
from views.settings_screen import SettingsScreen
from views.profile_screen import ProfileScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ProfileScreen(name='profile'))
        return sm

if __name__ == '__main__':
    MyApp().run()
