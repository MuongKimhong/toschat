from textual.widgets import Static, Header, Input, Button
from textual.containers import Container, Horizontal, Vertical
from textual.app import ComposeResult
from textual.screen import Screen


class SignUpScreen(Screen):
    CSS_PATH = "signup.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Create new account", classes="create-new-acc-text")
        yield Input(placeholder="Username", id="username-input")
        yield Input(placeholder="Password", password=True, classes="password-input")
        yield Input(placeholder="Confirm Password", password=True, classes="password-input")
        yield Container(
            Button("Sign Up", id="signup-btn", variant="success"),
            classes="container"
        )
        yield Static("Or", id="or-txt")
        yield Container(
            Button("Sign In with existing account", id="signin-btn", variant="default"),
            classes="container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "signin-btn":
            from ..signin_screen.signin import SignInScreen
            
            self.app.install_screen(SignInScreen, "signin")
            self.app.switch_screen("signin")
            self.app.uninstall_screen("signup")
