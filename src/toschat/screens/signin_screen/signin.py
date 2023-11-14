from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.app import ComposeResult
from textual.screen import Screen


class SignInScreen(Screen):
    CSS_PATH = "signin.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Sign In", classes="sign-in-text")
        yield Input(placeholder="Username", id="username-input")
        yield Input(placeholder="Password", password=True, id="password-input")
        yield Container(
            Button("Sign In", id="signin-btn", variant="primary"),
            id="container"
        )
        yield Static("Create new account", id="create-new-acc-text")
