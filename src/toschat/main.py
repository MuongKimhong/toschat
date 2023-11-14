from textual.app import App, ComposeResult

from screens.signin_screen.signin import SignInScreen
from screens.signup_screen.signup import SignUpScreen


class TosChat(App):
    SCREENS = {
        "signin": SignInScreen()
    } 
    
    def on_mount(self):
        self.push_screen("signin")


if __name__ == "__main__":
    app = TosChat()
    app.run()
