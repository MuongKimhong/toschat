from textual.widgets import ListItem, Static
from textual.containers import Container
from textual.app import ComposeResult
from textual import events

from styles.css import CONTACT_STYLES, CONTACT_LIST_ITEM_STYLES


class Contact(Container):
    DEFAULT_CSS = CONTACT_STYLES

    def __init__(self, username: str, room) -> None:
        self.username = username
        self.room = room
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(f"{self.username} - room {self.room}", classes="username")
        yield Static(">>", classes="arrow")


class ContactListItem(ListItem):
    DEFAULT_CSS = CONTACT_LIST_ITEM_STYLES

    def __init__(self, username: str, chatroom_id: int) -> None:
        self.username = username
        self.chatroom_id = chatroom_id
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Contact(username=self.username, room=self.chatroom_id)

    def watch_highlighted(self, value: bool) -> None:
        pass

    def on_click(self, event: events.Click) -> None:
        from screens.chat import ChatScreen
        self.app.current_chatroom_id = self.chatroom_id
        self.app.switch_screen(ChatScreen()) 
