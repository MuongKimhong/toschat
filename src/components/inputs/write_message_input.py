from textual.widgets import Input
from textual import events


class WriteMessageInput(Input, can_focus=True):
    DEFAULT_CSS = '''
    WriteMessageInput {
        color: white;
    }
    WriteMessageInput:focus {
        border: tall rgb(40, 40, 40);
    }
    WriteMessageInput>.input--cursor {
        background: $surface;
        color: $text;
        text-style: reverse;
    }
    '''

    def on_mount(self, event: events.Mount) -> None:
        self.focus()