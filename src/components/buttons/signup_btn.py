from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Button
from textual import events, log


class SignUpButton(Container, can_focus=True):
    DEFAULT_CSS = '''   
    SignUpButton {
        margin-top: 0;
        padding-top: 0;
        align: center middle;
        width: 100%;
        height: 5;
    }
    #signup-btn {
        content-align: center middle;
        width: 4; 
    }
    '''

    def compose(self) -> ComposeResult:
        yield Button("Sign Up", variant="default", id="signup-btn")