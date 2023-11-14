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
            classes="container"
        )
        yield Static("Or", id="or-txt")
        yield Container(
            Button("Create new account", id="create-new-acc-btn", variant="default"),
            classes="container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create-new-acc-btn":
            from ..signup_screen.signup import SignUpScreen

            self.app.install_screen(SignUpScreen, "signup")
            self.app.switch_screen("signup")
            self.app.uninstall_screen("signin")
