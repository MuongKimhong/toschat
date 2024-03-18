from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Button


class SignInWithExistAccountButton(Container, can_focus=True):
    DEFAULT_CSS = '''   
    SignInWithExistAccountButton {
        margin-top: 1;
        padding-top: 0;
        align: center middle;
        width: 100%;
        height: 3;
    }
    #signin-exist-acc-btn {
        content-align: center middle;
        width: 35; 
        height: 3;
        border: none;
    }
    '''

    def compose(self) -> ComposeResult:
        yield Button("Sign In with existing account", variant="default", id="signin-exist-acc-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        from screens.sign_in import SignInScreen
        self.app.switch_screen(SignInScreen())