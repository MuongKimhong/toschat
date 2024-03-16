from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Input
from textual.containers import Container
from textual import log, events

from components.inputs.username_input import UsernameInput
from components.inputs.password_input import PasswordInput
from components.buttons.signup_btn import SignUpButton
from components.buttons.signin_exist_acc_btn import SignInWithExistAccountButton
from components.error_message import ErrorMessage

from styles.css import SIGN_UP_SCREEN_STYLES
from api_requests import ApiRequests


class SignUpScreen(Screen):
    DEFAULT_CSS = SIGN_UP_SCREEN_STYLES
    api_requests = ApiRequests()

    def compose(self) -> ComposeResult:
        yield Static("Create New Account", id="create-new-account-txt")
        yield ErrorMessage("", id="signup-error-message")
        yield UsernameInput(
            placeholder="Enter username", 
            max_length=25,
            id="signup-username-input"
        )
        yield PasswordInput(
            placeholder="Enter password", 
            password=True, 
            max_length=25,
            id="signup-password-input"
        )
        yield PasswordInput(
            placeholder="Enter confirm password", 
            password=True, 
            max_length=25,
            id="signup-confirm-password-input"
        )
        yield SignUpButton()
        yield Static("or", id="or-txt")
        yield SignInWithExistAccountButton()

