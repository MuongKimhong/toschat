from textual.widgets import Input, Button, ListView, ListItem, Static
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from components.search_result_list_item import ResultListItem
from styles.css import (
    NEW_CONTACT_SCREEN_STYLES,
    SEARCH_RESULTS_CONTAINER_STYLES,
    NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES
)


class SearchResultUpperContainer(Container):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter contact name to search")
        yield Button("< Back", variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        from screens.contacts import ContactScreen
        self.app.switch_screen(ContactScreen())


class SearchResultContainer(Container):
    DEFAULT_CSS = SEARCH_RESULTS_CONTAINER_STYLES

    def compose(self) -> ComposeResult:
        results = [ResultListItem(f"username{i+1}") for i in range(20)]
        yield ListView(*results)


class NewContactScreen(Screen):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield SearchResultUpperContainer()
        yield SearchResultContainer()
