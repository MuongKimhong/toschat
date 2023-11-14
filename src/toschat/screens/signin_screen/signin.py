from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.app import ComposeResult
from textual.screen import Screen
from pathlib import Path
import requests
import time
import os

from ..variables import SERVER_BASE_URL


def sign_in(username, password):
    pass


class SignInScreen(Screen):
    CSS_PATH = "signin.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Sign In", classes="sign-in-text")
        yield Static("Username or password is incorrect", id="error-text")
        yield Input(placeholder="Username", id="username-input")
        yield Input(placeholder="Password", password=True, id="password-input")
        yield Container(
            Button("Sign In", id="signin-btn", variant="primary"),
            classes="container"
        )
        yield Static("Or", id="or-txt")
        yield Container(
            Button("Create new account", id="create-new-acc-btn", variant="default"),
            classes="container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create-new-acc-btn":
            from ..signup_screen.signup import SignUpScreen

            self.app.install_screen(SignUpScreen, "signup")
            self.app.switch_screen("signup")
            self.app.uninstall_screen("signin")

        elif event.button.id == "signin-btn":
            self.query_one("#error-text").styles.visibility = "hidden"
            username = self.query_one("#username-input").value
            password = self.query_one("#password-input").value

            if (username.strip() == "") or (password.strip() == ""):
                self.query_one("#error-text").styles.visibility = "visible"
                self.query_one("#username-input").styles.margin = (1, 12, 1, 12)
            else:
                home_dir = Path.home()

                # create an empty json file to store credential
                if os.path.exists(f"{home_dir}/toschat_cred.json") is False:
                    open(f"{home_dir}/toschat_cred.json", "a").close()                

