from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.app import ComposeResult
from textual.screen import Screen
from pathlib import Path
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL   


messages = [
    {"id": 1, "text": "Hello"},
    {"id": 2, "text": "Testing"},
    {"id": 3, "text": "What's up"}
]


def read_cred_file():
    path = f"{Path.home()}/toschat_cred.json"

    with open(path, "r") as cred_file:
        credential = json.load(cred_file)

    return credential  


class HomeScreen(Screen):
    CSS_PATH = "home.tcss"
    credential = None

    def compose(self) -> ComposeResult:
        self.credential = read_cred_file()
        
        yield Container(
            Horizontal(Button("Logout", id="logout")),
            id="top-container"
        )
    
    def logout(self):
        os.remove(f"{Path.home()}/toschat_cred.json")
        from ..signin_screen.signin import SignInScreen
        self.app.install_screen(SignInScreen, "signin")
        self.app.push_screen("signin")
        self.app.uninstall_screen("home")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "logout":
            self.logout()
