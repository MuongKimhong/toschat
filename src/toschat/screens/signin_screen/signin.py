from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.app import ComposeResult
from textual.screen import Screen
from pathlib import Path
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL


def sign_in(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{SERVER_BASE_URL}api-users/sign-in/", data)
    response = json.loads(response.text)

    if response.get("error") is True:
        return {"error": True}

    return {"error": False, "credential": response} 


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


    def display_error(self):
        self.query_one("#error-text").styles.visibility = "visible"
        self.query_one("#username-input").styles.margin = (1, 12, 1, 12)


    def redirect_home(self):
        if "home" not in self.app._installed_screens:
            from ..home_screen.home import HomeScreen
            self.app.install_screen(HomeScreen, "home")

        self.app.switch_screen("home")
        self.app.uninstall_screen("signin")


    def redirect_signup(self):
        if "signup" not in self.app._installed_screens:
            from ..signup_screen.signup import SignUpScreen
            self.app.install_screen(SignUpScreen, "signup")

        self.app.switch_screen("signup")
        self.app.uninstall_screen("signin")


    def create_credential_file(self, credential: dict) -> None:
        path = f"{Path.home()}/toschat_cred.json"

        # create an empty json file to store credential
        if os.path.exists(path) is False:
            open(path, "a").close()

        data_to_store = credential
        data_to_store["selected_username_to_message"] = ""
        data_to_store["selected_chatroom_id"] = ""
        data_to_store = json.dumps(data_to_store, indent=4)

        with open(path, "w") as cred_file:
            cred_file.write(data_to_store)


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create-new-acc-btn":
            self.redirect_signup()

        elif event.button.id == "signin-btn":
            self.query_one("#error-text").styles.visibility = "hidden"
            username = self.query_one("#username-input").value
            password = self.query_one("#password-input").value

            if (username.strip() == "") or (password.strip() == ""):
                self.display_error()
            else:
                response = sign_in(username, password)

                if response["error"] is True:
                    self.display_error()
                else:
                    self.create_credential_file(response["credential"])
                    self.redirect_home()
