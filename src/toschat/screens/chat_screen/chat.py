from textual.widgets import Static, Header, Input, Button
from textual.widgets import ListView, ListItem
from textual.containers import Container, Horizontal
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from rich.segment import Segment
from textual.strip import Strip
from pathlib import Path
from textual import events
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


class MessageWidget(Static):
    def compose(self) -> ComposeResult:
        '''
        renderable arg will be name-messagetextblahblah 
        renderable_split[0] is name
        renderable_split[1] is messagetextblahblahblah
        '''
        renderable_split = self.renderable.split("-")
        yield Static(f"{renderable_split[0]}: {renderable_split[1]}", classes="username")


class MessageAreaWidget(Widget):
    messages = [
        {"sender": "richard", "text": "Hello all friends"},
        {"sender": "erlich", "text": "whats up buddy"},
        {"sender": "roman", "text": "what a good day"},
        {"sender": "gilfoyle", "text": "shut the fuck up"},
        {"sender": "soap", "text": "all eyes on me"}
    ]
    messages_widget = reactive([]) 

    def compose(self) -> ComposeResult:
        for message in self.messages:
            self.messages_widget.append(
                ListItem(MessageWidget(f"{message['sender']}-{message['text']}"), classes="list-item")
            )

        yield Container(
            ListView(*self.messages_widget, initial_index=None, id="messages-list-view"),
            id="messages-container"
        )


class ChatScreen(Screen):
    CSS_PATH = "chat.tcss"
    credential = {}

    def compose(self) -> ComposeResult:
        with open(f"{Path.home()}/toschat_cred.json", "r") as cred_file:
            self.credential = json.load(cred_file)

        yield NavbarWidget()
        yield MessageAreaWidget()
        yield Input(placeholder="Write message here", id="message-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "message-input":
            self.query_one("#messages-list-view").append(
                ListItem(MessageWidget(f"{self.credential['user']['username']}-{event.input.value}"), 
                classes="list-item")
            )
            event.input.value = ""
