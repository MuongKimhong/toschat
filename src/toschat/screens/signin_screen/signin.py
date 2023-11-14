from textual.widgets import Static, Header
from textual.app import ComposeResult
from textual.screen import Screen


class SignInScreen(Screen):
    CSS_PATH = "signin.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Sign In Screen")  
