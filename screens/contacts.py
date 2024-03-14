from textual.widgets import Static, Button, Input, Label
from textual.widgets import ListView, ListItem
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from components.contact_list_item import ContactListItem

from styles.css import (
    CONTACT_SCREEN_STYLES,
    CONTACT_LIST_CONTAINER_STYLES,
    CONTACT_SCREEN_UPPER_CONTAINER_STYLES
)


class UpperContainer(Container):
    DEFAULT_CSS = CONTACT_SCREEN_UPPER_CONTAINER_STYLES

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Search contacts")
        yield Button("New", variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        from screens.new_contact import NewContactScreen
        self.app.switch_screen(NewContactScreen())


class ContactListContainer(Container):
    DEFAULT_CSS = CONTACT_LIST_CONTAINER_STYLES

    def compose(self) -> ComposeResult:
        contact_lists = [ContactListItem(f"username {i+1}") for i in range(15)]
        yield ListView(*contact_lists)


class ContactScreen(Screen, can_focus=True):
    DEFAULT_CSS = CONTACT_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield UpperContainer()
        yield ContactListContainer()
