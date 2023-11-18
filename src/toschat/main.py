from textual.app import App, ComposeResult

from screens.signin_screen.signin import SignInScreen
from screens.signup_screen.signup import SignUpScreen
from screens.home_screen.home import HomeScreen

from pathlib import Path
import json
import os


class TosChat(App):
    def on_mount(self):
        home_dir = Path.home()
        credential_file_path = f"{home_dir}/toschat_cred.json"

        # if toschat_cred.json file not exist, redirect to signin
        if os.path.exists(credential_file_path) is False:
            self.install_screen(SignInScreen, "signin")
            self.push_screen("signin")

        # # redirect home screen
        else:
            self.install_screen(HomeScreen, "home")
            self.push_screen("home") 
            

if __name__ == "__main__":
    app = TosChat()
    app.run()
