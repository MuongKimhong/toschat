from textual.widgets import Input, ListItem
from textual import events, log

from components.message import Message


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

    def on_input_submitted(self, event: Input.Submitted) -> None:
        message = event.value.strip()

        if message != "":
            self.app.query_one("ChatScreen").messages_list_view.append(
                ListItem(Message(
                    {
                        "sender": {"username": "current", "id": "2"},
                        "message": {"id": "4", "text": message}
                    }
                ))
                
            )
            self.value = ""