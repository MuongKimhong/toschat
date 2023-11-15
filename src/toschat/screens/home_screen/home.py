from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.app import ComposeResult
from textual.screen import Screen
from rich.segment import Segment
from textual.strip import Strip
from pathlib import Path
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL   


def read_cred_file() -> dict:
    path = f"{Path.home()}/toschat_cred.json"

    with open(path, "r") as cred_file:
        credential = json.load(cred_file)

    return credential  


def get_all_users(current_user_id: int, access_token: str) -> list:

    url = f"{SERVER_BASE_URL}api-users/list-all-users/"
    params = {"current_user_id": current_user_id}
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, params=params, headers=headers)
    response: dict = json.loads(response.text)

    return response["users"]


class HomeScreen(Screen):
    CSS_PATH = "home.tcss"
    credential = None
    all_users = []
    all_usernames = []

    def compose(self) -> ComposeResult:        
        self.credential = read_cred_file()
        self.all_users = get_all_users(self.credential["user"]["id"], self.credential["access_token"])
        self.all_usernames = [Static(user["username"], classes="username-text") for user in self.all_users]
        
        yield Container(
            Horizontal(Button("Logout", id="logout")),
            id="top-container"
        )
        yield ScrollableContainer(*self.all_usernames, id='user-list-container')
    
    def logout(self):
        os.remove(f"{Path.home()}/toschat_cred.json")
        
        if "signin" not in self.app._installed_screens:
            from ..signin_screen.signin import SignInScreen
            self.app.install_screen(SignInScreen, "signin")

        self.app.switch_screen("signin")
        self.app.uninstall_screen("home")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "logout":
            self.logout()
