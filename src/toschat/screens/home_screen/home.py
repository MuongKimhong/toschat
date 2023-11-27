from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.widgets import ListView, ListItem
from textual.app import ComposeResult
from textual.message import Message
from textual.screen import Screen
from rich.segment import Segment
from textual.strip import Strip
from pathlib import Path
from textual import events
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL   


class UserWidget(Static):
    def compose(self) -> ComposeResult:
        yield Static(self.renderable, classes="username-text")
        yield Button("message", classes="start-message-btn", id=f"{self.renderable}")


class HomeScreen(Screen):
    CSS_PATH = "home.tcss"
    all_users = []
    credential = None
    list_view = ListView(*[], id="list-view")
    credential_file_path = f"{Path.home()}/toschat_cred.json"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(Button("Logout", id="logout"), id="top-container")
        yield Input(placeholder="Search user", id="search-user-input")
        yield Container(self.list_view, id='user-list-container')

    def read_cred_file(self) -> None:
        with open(self.credential_file_path, "r") as cred_file:
            self.credential = json.load(cred_file)

    def logout(self): 
        if "signin" not in self.app._installed_screens:
            from ..signin_screen.signin import SignInScreen
            self.app.install_screen(SignInScreen, "signin")

        os.remove(f"{Path.home()}/toschat_cred.json")
        self.app.switch_screen("signin")

    def get_all_users(self) -> None:
        url = f"{SERVER_BASE_URL}api-users/list-all-users/"
        params = {"current_user_id": self.credential["user"]["id"]}
        headers = {"Authorization": f"Bearer {self.credential['access_token']}"}
        response = requests.get(url, params=params, headers=headers)
        self.all_users = json.loads(response.text)["users"]
        self.list_view.clear()
        
        for user in self.all_users:
            self.list_view.append(ListItem(UserWidget(user["username"]), classes="list-item"))

    def search_users(self, text: str) -> None:
        if text.strip() != "":
            url = f"{SERVER_BASE_URL}api-users/search-users/"
            params = {"current_user_id": self.credential["user"]["id"], "search_text": text}
            headers = {"Authorization": f"Bearer {self.credential['access_token']}"}
            response  = requests.get(url, params=params, headers=headers)
            users: list = json.loads(response.text)["users"]
            self.list_view.clear()

            for user in users:
                self.list_view.append(ListItem(UserWidget(user), classes="list-item"))
        else:
            self.get_all_users()

    def start_message(self, username: str) -> None:
        url = f"{SERVER_BASE_URL}api-chats/start-message-user/" 
        data = {"other_username": username}
        headers = {"Authorization": f"Bearer {self.credential['access_token']}"}
        response = requests.post(url, data=data, headers=headers)
        response = json.loads(response.text)

        path = f"{Path.home()}/toschat_cred.json" 
        self.credential["selected_chatroom_id"] = response["chatroom_id"]
        self.credential["selected_username_to_message"] = username

        with open(path, "w") as cred_file:
            cred_file.write(json.dumps(self.credential, indent=4))

        # redirect to chatscreen
        if "chat" not in self.app._installed_screens:
            from ..chat_screen.chat import ChatScreen
            self.app.install_screen(ChatScreen, "chat")

        self.app.switch_screen("chat")

    def clear_data(self) -> None:
        self.all_users.clear()
        self.list_view.clear()
        self.credential = None

    def on_screen_resume(self, event: events.ScreenResume) -> None:
        self.read_cred_file()
        self.get_all_users()

    def on_screen_suspend(self, event: events.ScreenSuspend) -> None:
        self.clear_data()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "logout":
            self.logout()
        else:
            self.start_message(username=event.button.id)
    
    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "search-user-input":
            self.search_users(event.input.value)