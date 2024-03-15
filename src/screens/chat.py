from typing import Dict

from textual.widgets import Button, Static, ListView, ListItem, TextArea
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from components.inputs.write_message_input import WriteMessageInput
from components.message import Message

from styles.css import CHAT_SCREEN_STYLES, MESSAGES_CONTAINER_STYLES

import api_requests


class MessagesContainer(Container, can_focus=True):
    DEFAULT_CSS = MESSAGES_CONTAINER_STYLES

    def __init__(self, messages_list_view: ListView) -> None:
        self.messages_list_view = messages_list_view
        super().__init__()

    def compose(self) -> ComposeResult:
        yield self.messages_list_view


class ChatScreen(Screen):
    DEFAULT_CSS = CHAT_SCREEN_STYLES

    messages_list_view = ListView(*[], id="messages-list-view")

    def compose(self) -> ComposeResult:
        yield Button("< Back", id="back-btn")
        yield MessagesContainer(messages_list_view=self.messages_list_view)
        yield WriteMessageInput(placeholder="Write message")

    def on_screen_resume(self, event: events.ScreenResume) -> None:
        messages: list[Dict[str, Dict[str, str]]] = api_requests.get_messages()

        for message in messages:
            self.messages_list_view.append(ListItem(Message(message)))

        self.messages_list_view.scroll_end()
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            from screens.contacts import ContactScreen
            self.app.switch_screen(ContactScreen()) 

    def on_mount(self, event: events.Mount) -> None:
        pass
