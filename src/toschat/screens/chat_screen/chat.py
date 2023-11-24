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
from textual import work
from textual import events
from textual.message import Message
import threading
import socketio
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL


websocket = socketio.SimpleClient()
websocket.connect("http://localhost:3000")


def restart_app():
    while True:
        if restart is True:
            import sys
            os.execv(sys.executable, ['python3'] + sys.argv)

restart_thread = threading.Thread(target=restart_app)
restart_thread.start()


class WebSocketReceivingThread(threading.Thread):
    def listen_websocket_receive_event(self):
        while True:
            event = websocket.receive()
            if event[0] == "newmessage":
                path = f"{Path.home()}/Development/toschat/joymisoussreaymean.json"
                open(path, "a").close() 
        
    def run(self):
        try:
            self.listen_websocket_receive_event()
        except BaseException as e:
            raise e


def read_test_file():
    path = f"{Path.home()}/database.json"

    with open(path, "r") as database_file:
            data = json.load(database_file)["messages"]    
            
    return data


def write_test_file(data):
    path = f"{Path.home()}/database.json"

    old_data = read_test_file()
    old_data.append(data)

    with open(path, "w") as database_file:
        database_file.write(json.dumps({"messages": old_data}, indent=4))


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
    class Receive(Message):
        def __init__(self, event) -> None:
            self.event = event
            super().__init__()
    
    def __init__(self) -> None:
        self.list_view = ListView(*[], id="messages-list-view")
        super().__init__()

    def compose(self) -> ComposeResult: 
        messages = read_test_file()

        yield Container(self.list_view, id="messages-container")

        for message in messages:
            self.list_view.append(
                ListItem(MessageWidget(f"{message['sender']}-{message['text']}"), classes="list-item")
            ) 
        self.websocket_receive()
        
    @work(exclusive=True, thread=True)
    def websocket_receive(self):
        while True:
            event = websocket.receive()
            if event[0] == "newmessage":
                path = f"{Path.home()}/Development/toschat/joymisous.json"

                # create an empty json file to store credential
                if os.path.exists(path) is False:
                    open(path, "a").close()

                self.post_message(self.Receive(event[1]))

class ChatScreen(Screen):
    CSS_PATH = "chat.tcss"
    credential = {}

    def compose(self) -> ComposeResult:
        with open(f"{Path.home()}/toschat_cred.json", "r") as cred_file:
            self.credential = json.load(cred_file)
        
        yield NavbarWidget()
        yield MessageAreaWidget()
        yield Input(placeholder="Write message here", id="message-input") 
    
    def on_message_area_widget_receive(self, message: MessageAreaWidget.Receive) -> None:
        self.query_one(MessageAreaWidget).list_view.append(
            ListItem(MessageWidget(f"{message.event['sender']}-{message.event['text']}"), classes="list-item")
        )
                
    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "message-input":
            if event.input.value != "":
                write_test_file({"sender": f"{self.credential['user']['username']}", "text": event.input.value})
                websocket.emit("send message", {"sender": f"{self.credential['user']['username']}", "text": event.input.value})        
                event.input.value = ""
