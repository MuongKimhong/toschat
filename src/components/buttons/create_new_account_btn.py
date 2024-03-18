from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Button


class CreateNewAccountButton(Container, can_focus=True):
    DEFAULT_CSS = '''   
    CreateNewAccountButton {
        margin-top: 1;
        padding-top: 0;
        align: center middle;
        width: 100%;
        height: 3;
    }
    #create-new-account-btn {
        content-align: center middle;
        width: 22; 
        height: 3;
        border: none;
    }
    '''

    def compose(self) -> ComposeResult:
        yield Button("Create New Account", variant="default", id="create-new-account-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        from screens.sign_up import SignUpScreen
        self.app.switch_screen(SignUpScreen())
