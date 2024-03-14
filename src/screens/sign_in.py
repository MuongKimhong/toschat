from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual.containers import Container

from components.inputs.username_input import UsernameInput
from components.inputs.password_input import PasswordInput
from components.buttons.signin_btn import SignInButton
from components.buttons.create_new_account_btn import CreateNewAccountButton

from styles.css import SIGN_IN_SCREEN_STYLES


class SignInScreen(Screen):
    DEFAULT_CSS = SIGN_IN_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield Static("Sign In", id="sign-in-txt")
        yield UsernameInput(placeholder="Enter username")
        yield PasswordInput(placeholder="Enter password", password=True)
        yield SignInButton()
        yield Static("or", id="or-txt")
        yield CreateNewAccountButton()
