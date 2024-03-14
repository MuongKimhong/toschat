from textual.widgets import Button, Input, Static, ListView, ListItem
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from styles.css import CHAT_SCREEN_STYLES


class ChatScreen(Screen):
    DEFAULT_CSS = CHAT_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield Static("hello chatscreen")
