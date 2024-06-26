from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual import events

from components.buttons.create_new_account_btn import CreateNewAccountButton
from components.inputs.username_input import UsernameInput
from components.inputs.password_input import PasswordInput
from components.buttons.signin_btn import SignInButton
from components.please_wait_text import PleaseWaitText
from components.error_message import ErrorMessage
from components.header import TosChatHeader

from styles.css import SIGN_IN_SCREEN_STYLES


class SignInScreen(Screen):
    DEFAULT_CSS = SIGN_IN_SCREEN_STYLES

    def __init__(self) -> None:
        self.screen_name = "SignInScreen"
        super().__init__()

    def compose(self) -> ComposeResult:
        yield TosChatHeader()
        yield Static("Sign In", id="sign-in-txt")
        yield PleaseWaitText("Please wait ....", id="signin-pls-wait-txt")
        yield ErrorMessage("", id="signin-error-message")
        yield UsernameInput(
            placeholder="Enter username",
            max_length=25,
            id="signin-username-input"
        )
        yield PasswordInput(
            placeholder="Enter password", 
            password=True,
            max_length=25,
            id="signin-password-input"
        )
        yield SignInButton()
        yield Static("or", id="or-txt")
        yield CreateNewAccountButton()

    def on_key(self, event: events.Key) -> None:
        if (event.key == "enter"):
            focused_widget = self.app.focused

            if (focused_widget.id == "signin-btn") or (focused_widget.id == "signin-password-input"):
                self.query_one("#signin-btn").press()

            elif focused_widget.id == "create-new-account-btn":
                self.query_one("#create-new-account-btn").press()
