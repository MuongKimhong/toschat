from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

from components.buttons.signin_exist_acc_btn import SignInWithExistAccountButton
from components.inputs.username_input import UsernameInput
from components.inputs.password_input import PasswordInput
from components.buttons.signup_btn import SignUpButton
from components.please_wait_text import PleaseWaitText
from components.error_message import ErrorMessage
from components.header import TosChatHeader

from styles.css import SIGN_UP_SCREEN_STYLES
from api_requests import ApiRequests


class SignUpScreen(Screen):
    DEFAULT_CSS = SIGN_UP_SCREEN_STYLES
    api_requests = ApiRequests()

    def compose(self) -> ComposeResult:
        yield TosChatHeader()
        yield Static("Create New Account", id="create-new-account-txt")
        yield PleaseWaitText("Please wait ...", id="signup-pls-wait-txt")
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

