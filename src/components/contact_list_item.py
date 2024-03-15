from textual.widgets import ListItem, Static
from textual.containers import Container
from textual.app import ComposeResult
from textual.color import Color
from textual import events, log

from styles.css import CONTACT_STYLES, CONTACT_LIST_ITEM_STYLES


class Contact(Container):
    DEFAULT_CSS = CONTACT_STYLES

    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(self.username, classes="username")
        yield Static(">>", classes="arrow")


class ContactListItem(ListItem):
    DEFAULT_CSS = CONTACT_LIST_ITEM_STYLES

    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Contact(username=self.username)

    def watch_highlighted(self, value: bool) -> None:
        pass

    def on_click(self, event: events.Click) -> None:
        from screens.chat import ChatScreen
        self.app.switch_screen(ChatScreen()) 
