from textual.app import ComposeResult
from textual import events, log
from textual.widgets import Static, Input


class UsernameInput(Input, can_focus=True):
    DEFAULT_CSS = '''
    UsernameInput {
        margin-top: 1;
        margin-bottom: 1;
    }
    '''

    def on_mount(self, event: events.Mount) -> None:
        pass
