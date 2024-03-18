from textual.widgets import Input
from textual import events


class PasswordInput(Input, can_focus=True):
    DEFAULT_CSS = '''
    PasswordInput {
        margin-top: 1;
        margin-bottom: 1;
    }
    '''

    def on_key(self, event: events.Key) -> None:
        if event.key == "space":
            event.prevent_default()