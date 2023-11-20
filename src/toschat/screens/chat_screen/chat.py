from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal
from textual.widgets import ListView, ListItem
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from rich.segment import Segment
from textual.strip import Strip
from pathlib import Path
from textual import events
import threading
import socketio
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL


websocket = socketio.SimpleClient()
websocket.connect("http://localhost:3000")


def create_test_file():
    path = f"{Path.home()}/Development/toschat/database.json"

    # create an empty json file to store credential
    if os.path.exists(path) is False:
        open(path, "a").close()

        with open(path, "w") as database_file:
            database_file.wirte(json.dumps({"messages": []}, indent=4))


def read_test_file():
    path = f"{Path.home()}/Development/toschat/database.json"

    with open(path, "r") as database_file:
            data = json.load(database_file)["messages"]    
            
    return data


def write_test_file(data):
    path = f"{Path.home()}/Development/toschat/database.json"

    old_data = read_test_file()
    old_data.append(data)

    with open(path, "w") as database_file:
        database_file.write(json.dumps(old_data))


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
    list_view = reactive(ListView(*[], id="messages-list-view"), always_update=True)

    def compose(self) -> ComposeResult: 
        create_test_file()
        messages = read_test_file()

        yield Container(self.list_view, id="messages-container")

        for message in messages:
            self.list_view.append(
                ListItem(MessageWidget(f"{message['sender']}-{message['text']}"), classes="list-item")
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
    
    def websocket_receive(self):
        while True:
            event = websocket.receive()
            if event[0] == "newmessage":
                self.query_one(MessageAreaWidget) = self.query_one(MessageAreaWidget).refresh()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "message-input":
            if event.input.value != "":
                write_test_file({"sender": f"{self.credential['user']['username']}", "text": event.input.value})
                websocket.emit("send message", {"sender": f"{self.credential['user']['username']}", "text": event.input.value})        
                event.input.value = ""
