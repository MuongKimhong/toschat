from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Static
from textual import events


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

    @property
    def message_is_type_date(self) -> bool:
        return True if self.message["type"] == "date" else False

    @property
    def message_is_sender_message(self) -> bool:
        if self.message["sender"]["id"] == self.app.user["id"]:
            return True
            
        return False

    def compose(self) -> ComposeResult:
        if self.message_is_type_date:
            classes = "date"
            message_text = self.message["message"]["text"]

        else:            
            if self.message_is_sender_message:
                classes = "right-message"
                message_text = self.message["message"]["text"]

            else:
                classes = "left-message"
                message_text = f"{self.message['sender']['username']}: {self.message['message']['text']}"

        yield Static(
            renderable=message_text,
            classes=classes,
            id=f"message-text-{self.message['message']['id']}"
        )