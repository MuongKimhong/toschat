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


class ChatScreen(Screen):
    CSS_PATH = "chat.tcss"

    def compose(self) -> ComposeResult:
        yield Static("Chatscreen")
