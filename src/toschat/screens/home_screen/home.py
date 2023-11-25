from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.app import ComposeResult
from textual.message import Message
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


def start_message_user(username: str, access_token: str) -> None:

    url = f"{SERVER_BASE_URL}api-chats/start-message-user/" 
    data = {"other_username": username}
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.post(url, data=data, headers=headers)
    response = json.loads(response.text)

    path = f"{Path.home()}/toschat_cred.json"

    credential = None
    with open(path, "r") as cred_file:
        credential = json.load(cred_file) 

    data_to_store = credential
    data_to_store["selected_chatroom_id"] = response["chatroom_id"]

    with open(path, "w") as cred_file:
        cred_file.write(json.dumps(data_to_store, indent=4))


def search_users_by_name(current_user_id: int, access_token: str, search_text: str) -> list:
    url = f"{SERVER_BASE_URL}api-users/search-users/"
    params = {"current_user_id": current_user_id, "search_text": search_text}
    headers = {"Authorization": f"Bearer {access_token}"}

    response  = requests.get(url, params=params, headers=headers)
    response: dict = json.loads(response.text)

    return response["users"]


class UserWidget(Static):
    def compose(self) -> ComposeResult:
        yield Static(self.renderable, classes="username-text")
        yield Button("message", classes="start-message-btn", name=f"{self.renderable}")


class HomeScreen(Screen):
    CSS_PATH = "home.tcss"
    credential = None
    all_users = []
    all_usernames_widget = []
    all_usernames_text = []

    def compose(self) -> ComposeResult:        
        self.credential = read_cred_file()
        if len(self.all_users) == 0:
            self.all_users = get_all_users(self.credential["user"]["id"], self.credential["access_token"])

            for user in self.all_users:
                self.all_usernames_widget.append(UserWidget(user["username"])) 
                self.all_usernames_text.append(user["username"])

        yield Container(Button("Logout", id="logout"), id="top-container")
        yield Input(placeholder="Search user", id="search-user-input")
        yield ScrollableContainer(*self.all_usernames_widget, id='user-list-container')
        
    
    def logout(self):
        os.remove(f"{Path.home()}/toschat_cred.json")
        
        if "signin" not in self.app._installed_screens:
            from ..signin_screen.signin import SignInScreen
            self.app.install_screen(SignInScreen, "signin")

        self.app.push_screen("signin")

    
    def redirect_chatscreen(self):
        if "chat" not in self.app._installed_screens:
            from ..chat_screen.chat import ChatScreen
            self.app.install_screen(ChatScreen, "chat")

        self.app.push_screen("chat")


    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "search-user-input":

            if self.query_one("#search-user-input").value.strip() != "":
                new_usernames = search_users_by_name(
                    current_user_id=self.credential["user"]["id"], 
                    access_token=self.credential["access_token"],
                    search_text=self.query_one("#search-user-input").value
                )
                for index, widget in enumerate(self.query(".username-text")):
                    if index < len(new_usernames):
                        widget.update(new_usernames[index])
                    else:
                        break
            else:
                for index, widget in enumerate(self.query(".username-text")):
                    widget.update(self.all_usernames_text[index])


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "logout":
            self.logout()
        else:
            path = f"{Path.home()}/toschat_cred.json"

            '''
            update selected_username_to_message in toschat_cred.json.
            update it because we want to use it to make request in start_message_user func
            '''
            for index, button in enumerate(self.query(".start-message-btn")):
                if button.name == event.button.name:
                    self.credential["selected_username_to_message"] = str(self.query(".username-text")[index].renderable)
                    break

            with open(path, "w") as cred_file:
                cred_file.write(json.dumps(self.credential, indent=4))
            
            start_message_user(self.credential["selected_username_to_message"], self.credential["access_token"])
            self.redirect_chatscreen()
