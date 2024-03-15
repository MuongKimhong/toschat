from textual.widgets import Button, Static, ListView, ListItem, TextArea
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from components.inputs.write_message_input import WriteMessageInput
from styles.css import CHAT_SCREEN_STYLES


class MessagesContainer(Container, can_focus=True):
    DEFAULT_CSS = '''
    MessagesContainer {
        padding: 1 1;
        border: round grey;
        border-top: hidden grey;
        border-left: hidden grey;
        border-right: hidden grey;
        color: white;
        height: 90%;
    }
    '''

    def compose(self) -> ComposeResult:
        yield Static("Container")


class ChatScreen(Screen):
    DEFAULT_CSS = CHAT_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield Button("< Back", id="back-btn")
        yield MessagesContainer()
        yield WriteMessageInput(placeholder="Write message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            from screens.contacts import ContactScreen
            self.app.switch_screen(ContactScreen())

    def on_mount(self, event: events.Mount) -> None:
        pass
