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


class NavbarWidget(Static):
    def compose(self) -> ComposeResult:
        with open(f"{Path.home()}/toschat_cred.json", "r") as cred_file:
            another_username = json.load(cred_file)["selected_username_to_message"]

        yield Button("< Back", id="back-btn")
        yield Static(another_username, id="another-username")
        yield Button("Logout", id="logout-btn")
    
    def redirect_homescreen(self):
        if "home" not in self.app._installed_screens:
            from ..home_screen.home import HomeScreen
            self.app.install_screen(HomeScreen, "home")
        
        self.app.switch_screen("home")
        self.app.uninstall_screen("chat")

    def logout(self):
        os.remove(f"{Path.home()}/toschat_cred.json")
        
        if "signin" not in self.app._installed_screens:
            from ..signin_screen.signin import SignInScreen
            self.app.install_screen(SignInScreen, "signin")

        self.app.switch_screen("signin")
        self.app.uninstall_screen("chat")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.redirect_homescreen()
        elif event.button.id == "logout-btn":
            self.logout()


class ChatScreen(Screen):
    CSS_PATH = "chat.tcss"

    def compose(self) -> ComposeResult:
        yield NavbarWidget()
