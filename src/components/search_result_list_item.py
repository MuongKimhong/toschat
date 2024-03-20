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
            yield Button(
                label="Added", 
                classes="add-btn", 
                id=str(self.username), 
                variant="default", 
                disabled=True
            )
        else:
            yield Button(
                label="Add", 
                classes="add-btn", 
                id=str(self.username), 
                variant="default",
                disabled=False
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        res = ApiRequests().add_new_contact_request(
            contact_username=self.username,
            access_token=self.app.access_token
        )
        if res["status_code"] == 200:
            if not event.button.disabled:
                self.added = True
                event.button.disabled = True
                event.button.label = "Added"


class ResultListItem(ListItem):
    DEFAULT_CSS = RESULT_LIST_ITEM_STYLES

    def __init__(self, username: str, added: bool, empty_result=False) -> None:
        self.username = username
        self.added = added
        self.empty_result = empty_result
        super().__init__()

    def compose(self) -> ComposeResult:
        if self.empty_result:
            yield Static("Search contacts by typing their names", id="empty-result-txt")
        else:
            yield Result(username=self.username, added=self.added)

    def watch_highlighted(self, value: bool) -> None:
        pass