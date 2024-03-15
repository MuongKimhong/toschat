from typing import Dict

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
    }
    .left-message {
        content-align: left middle;
        text-style: bold;
    }
    '''

    def __init__(self, message: Dict[str, Dict[str, str]]) -> None:
        self.message = message
        super().__init__()

    def compose(self) -> ComposeResult:
        if self.message["sender"]["id"] == "2":
            text = self.message["message"]["text"] 
            classes = "right-message"
        else:
            text = f"{self.message['sender']['username']}: {self.message['message']['text']}"
            classes = "left-message"

        yield Static(text, id=f"message-text-{self.message['message']['id']}", classes=classes)
