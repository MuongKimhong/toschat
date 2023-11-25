from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events
import requests
import json

from ..variables import SERVER_BASE_URL


def sign_up(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{SERVER_BASE_URL}api-users/sign-up/", data) 
    response = json.loads(response.text)

    if response.get("username_taken") is True:
        return {"error": True, "message": "Username is already taken"}

    return {"error": False}


class SignUpScreen(Screen):
    CSS_PATH = "signup.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Create new account", classes="create-new-acc-text")
        yield Static("", id="error-text")
        yield Input(placeholder="Username", id="username-input")
        yield Input(placeholder="Password", password=True, id="password-input")
        yield Input(placeholder="Confirm Password", password=True, id="confirm-password-input")
        yield Container(
            Button("Sign Up", id="signup-btn", variant="success"),
            classes="container"
        )
        yield Static("Or", id="or-txt")
        yield Container(
            Button("Sign In with existing account", id="signin-btn", variant="default"),
            classes="container"
        )

    def display_error(self, txt):
        self.query_one("#error-text").update(txt)
        self.query_one("#error-text").styles.visibility = "visible"

    def redirect_signin(self):
        if "signin" not in self.app._installed_screens:
            from ..signin_screen.signin import SignInScreen
            self.app.install_screen(SignInScreen, "signin")

        self.app.push_screen("signin")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "signin-btn":
            self.redirect_signin()
        
        elif event.button.id == "signup-btn":
            self.query_one("#error-text").styles.visibility = "hidden"
            username = self.query_one("#username-input").value
            password = self.query_one("#password-input").value
            c_password = self.query_one("#confirm-password-input").value

            if (username.strip() == "") or (password.strip() == "") or (c_password.strip() == ""):
                self.display_error("Information missing")
            elif password != c_password:
                self.display_error("Two passwords did not match")
            else:
                response = sign_up(username, password)

                if response["error"] is True:
                    self.display_error(response["message"])
                else:
                    self.redirect_signin() 
