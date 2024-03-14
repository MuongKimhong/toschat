from textual.widgets import Static, Button, ListItem
from textual.containers import Container
from textual.app import ComposeResult

from styles.css import RESULT_STYLES, RESULT_LIST_ITEM_STYLES


class Result(Container):
    DEFAULT_CSS = RESULT_STYLES

    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(self.username, classes="username")
        yield Button("Add", classes="add-btn", variant="default")


class ResultListItem(ListItem):
    DEFAULT_CSS = RESULT_LIST_ITEM_STYLES

    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Result(username=self.username)

    def watch_highlighted(self, value: bool) -> None:
        pass