from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual.containers import Container

from components.inputs.username_input import UsernameInput
from components.inputs.password_input import PasswordInput
from components.buttons.signup_btn import SignUpButton
from components.buttons.signin_exist_acc_btn import SignInWithExistAccountButton

from styles.css import SIGN_UP_SCREEN_STYLES


class SignUpScreen(Screen):
    DEFAULT_CSS = SIGN_UP_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield Static("Create New Account", id="create-new-account-txt")
        yield UsernameInput(placeholder="Enter username")
        yield PasswordInput(placeholder="Enter password", password=True)
        yield PasswordInput(placeholder="Enter confirm password", password=True)
        yield SignUpButton()
        yield Static("or", id="or-txt")
        yield SignInWithExistAccountButton()