from textual.widgets import ListItem, Static
from textual.containers import Container
from textual.app import ComposeResult
from textual import events, work

from styles.css import CONTACT_STYLES, CONTACT_LIST_ITEM_STYLES
from screens.chat import ChatScreen


class Contact(Container):
    DEFAULT_CSS = CONTACT_STYLES

    def __init__(self, username: str, is_online: bool) -> None:
        self.is_online = is_online
        self.username = username
        super().__init__()

    def compose(self) -> ComposeResult:
        if self.is_online:
            yield Static(
                renderable=f"{self.username} (online)", 
                classes="username-online", 
                id=f"contact-{self.username}"
            )
        else:
            yield Static(
                renderable=self.username, 
                classes="username", 
                id=f"contact-{self.username}"
            )

        yield Static(">>", classes="arrow")            


class ContactListItem(ListItem):
    DEFAULT_CSS = CONTACT_LIST_ITEM_STYLES

    def __init__(self, username: str, is_online: bool, chatroom_id: int, empty_contact=False) -> None:
        self.is_online = is_online
        self.username = username
        self.chatroom_id = chatroom_id
        self.empty_contact = empty_contact
        super().__init__()

    def compose(self) -> ComposeResult:
        if self.empty_contact:
            yield Static("You have no contacts at the moment.", id="empty-contact-txt")
        else:
            yield Contact(username=self.username, is_online=self.is_online)

    def watch_highlighted(self, value: bool) -> None:
        pass

    def on_click(self, event: events.Click) -> None:
        self.app.current_chat_username = self.username
        self.app.current_chatroom_id = self.chatroom_id
        self.app.switch_screen(ChatScreen()) 
