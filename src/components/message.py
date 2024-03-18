from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Static


class Message(Container):
    DEFAULT_CSS = '''
    Message {
        background: rgb(18, 18, 18);
    }
    .right-message {
        content-align: right middle;
        color: greenyellow;
        text-style: bold;
        padding-right: 1;
    }
    .left-message {
        content-align: left middle;
        text-style: bold;
    }
    .date {
        content-align: center middle;
    }
    '''

    def __init__(self, message) -> None:
        self.message = message
        super().__init__()

    def compose(self) -> ComposeResult:
        message = self.message["message"]

        if self.message["type"] == "date":
            text = message["text"]
            classes = "date"
        else:
            sender = self.message["sender"]

            if sender["id"] == self.app.user["id"]:
                text = message["text"]
                classes = "right-message"
            else:
                text = f"{sender['username']}: {message['text']}"
                classes = "left-message"

        yield Static(
            text, 
            id=f"message-text-{self.message['message']['id']}", 
            classes=classes
        )
