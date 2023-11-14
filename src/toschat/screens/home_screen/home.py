from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.app import ComposeResult
from textual.screen import Screen
from pathlib import Path
import requests
import time
import json
import os

from ..variables import SERVER_BASE_URL


class HomeScreen(Screen):
    CSS_PATH = "home.tcss"

    def compose(self) -> ComposeResult:
        yield Static("Home screen")
        yield Static("Testing", id="test")
