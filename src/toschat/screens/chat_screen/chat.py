from textual.widgets import Static, Header, Input, Button
from textual.worker import Worker, get_current_worker, NoActiveWorker
from textual.containers import Container, Horizontal
from textual.widgets import ListView, ListItem
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.message import Message
from textual.screen import Screen
from textual.widget import Widget
from textual import log
from pathlib import Path
from textual import work, events
import socketio
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL


class NavbarWidget(Static):
    class Leave(Message):
        def __init__(self):
            super().__init__()
    
    def compose(self) -> ComposeResult: 
        yield Button("< Back", id="back-btn")
        yield Static("", id="another-username")
        yield Button("Logout", id="logout-btn")
    
    def redirect_homescreen(self):
        if "home" not in self.app._installed_screens:
            from ..home_screen.home import HomeScreen
            self.app.install_screen(HomeScreen, "home")

        self.app.switch_screen("home") 

    def logout(self):
        os.remove(f"{Path.home()}/toschat_cred.json")
        
        if "signin" not in self.app._installed_screens:
            from ..signin_screen.signin import SignInScreen
            self.app.install_screen(SignInScreen, "signin")

        self.app.switch_screen("signin")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.post_message(self.Leave())
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


class Receive(Message):
    def __init__(self, new_message) -> None:
        self.new_message = new_message
        super().__init__()


class ChatScreen(Screen):
    CSS_PATH = "chat.tcss" 
    websocket = None
    credential = None
    list_view = ListView(*[], id="messages-list-view")
    another_username = None

    
    def compose(self) -> ComposeResult:
        yield NavbarWidget()
        yield Container(self.list_view, id="messages-container")
        yield Input(placeholder="Write message here", id="message-input")


    def clear_data(self):
        self.websocket = None
        self.credential = None
        self.list_view.clear()
        self.another_username = None

    
    def get_messages_in_chatroom(self):
        url = f"{SERVER_BASE_URL}api-chats/get-messages/"
        params = {"chatroom_id": self.credential['selected_chatroom_id']}
        headers = {"Authorization": f"Bearer {self.credential['access_token']}"}

        response = requests.get(url, params=params, headers=headers)
        messages: list = json.loads(response.text)["messages"]

        messages_widget = []

        for message in messages:
            message_widget = MessageWidget(f"{message['sender']['username']}-{message['text']}")
            self.list_view.append(ListItem(message_widget, classes="list-item"))

        self.list_view.scroll_end()

    
    def send_message(self, text: str):
        url = f"{SERVER_BASE_URL}api-chats/send-message/"
        data = {
            "chatroom_id": self.credential['selected_chatroom_id'], 
            "another_username": self.another_username,
            "text": text
        }
        headers = {"Authorization": f"Bearer {self.credential['access_token']}"}

        response = requests.post(url, data=data, headers=headers)
        message: dict = json.loads(response.text)["message"]
        self.websocket.emit("send message", message)

    
    @work(exclusive=True, thread=True)
    def websocket_receive(self):
        while True:
            event = self.websocket.receive()
            if event[0] == "newmessage":
                self.post_message(Receive(event[1]))


    def on_screen_resume(self, event: events.ScreenResume) -> None:

        # update username on navbar based on cred_file
        with open(f"{Path.home()}/toschat_cred.json", "r") as cred_file:
            self.credential = json.load(cred_file)
            self.another_username = self.credential["selected_username_to_message"]
            self.query_one("#another-username").update(self.another_username)

        # cancel worker
        try:
            current_worker = get_current_worker()
            if current_worker.is_running:
                current_worker.cancel()
        except NoActiveWorker:
            pass

        # connect websocket
        self.websocket = socketio.SimpleClient()
        self.websocket.connect("http://localhost:3000")

        # get messages
        self.get_messages_in_chatroom()

        # listen to websocket event
        self.websocket_receive()


    def on_screen_suspend(self, event: events.ScreenSuspend) -> None:
        # disconnect websocket
        self.websocket.disconnect()
        
        # cancel worker
        try:
            current_worker = get_current_worker()
            if current_worker.is_running:
                current_worker.cancel()
        except NoActiveWorker:
            pass

        # clear data
        self.clear_data()

    
    def on_receive(self, message: Receive) -> None:
        message_receiver = message.new_message["receiver"]["username"]
        message_sender   = message.new_message["sender"]["username"]
        current_username = self.credential["user"]["username"]

        if (current_username == message_receiver) or (current_username == message_sender):
            message_widget = MessageWidget(f"{message.new_message['sender']['username']}-{message.new_message['text']}")
            self.list_view.append(
                ListItem(message_widget, classes="list-item")
            )


    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "message-input":
            if event.input.value != "":
                self.send_message(event.input.value)
                event.input.value = ""
