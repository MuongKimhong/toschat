from textual.widgets import Static, Button, ListItem
from textual.containers import Container
from textual.app import ComposeResult

from styles.css import RESULT_STYLES, RESULT_LIST_ITEM_STYLES
from api_requests import ApiRequests


class Result(Container):
    DEFAULT_CSS = RESULT_STYLES

    def __init__(self, username: str, added: bool) -> None:
        self.username = username
        self.added = added
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(self.username, classes="username")

        if self.added:
            yield Button("Added", classes="add-btn", variant="default", disabled=True)
        else:
            yield Button("Add", classes="add-btn", variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        res = ApiRequests().add_new_contact_request(
            contact_username=self.username,
            access_token=self.app.access_token
        )
        if res["status_code"] == 200:
            from screens.contacts import ContactScreen
            self.app.switch_screen(ContactScreen())


class ResultListItem(ListItem):
    DEFAULT_CSS = RESULT_LIST_ITEM_STYLES

    def __init__(self, username: str, added: bool) -> None:
        self.username = username
        self.added = added
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Result(username=self.username, added=self.added)

    def watch_highlighted(self, value: bool) -> None:
        pass