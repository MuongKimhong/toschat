from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

from components.buttons.create_new_account_btn import CreateNewAccountButton
from components.inputs.username_input import UsernameInput
from components.inputs.password_input import PasswordInput
from components.buttons.signin_btn import SignInButton
from components.error_message import ErrorMessage

from styles.css import SIGN_IN_SCREEN_STYLES


class SignInScreen(Screen):
    DEFAULT_CSS = SIGN_IN_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield Static("Sign In", id="sign-in-txt")
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
