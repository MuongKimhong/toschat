from textual.widgets import Input, Button, ListView, ListItem, Static
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from components.search_result_list_item import ResultListItem
from api_requests import ApiRequests
from styles.css import (
    NEW_CONTACT_SCREEN_STYLES,
    SEARCH_RESULTS_CONTAINER_STYLES,
    NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES
)


class SearchResultUpperContainer(Container):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES
    api_request = ApiRequests()

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter contact name to search")
        yield Button("< Back", variant="default", id="go-back-btn")
        yield Button("Logout", variant="default", id="logout")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back-btn":
            from screens.contacts import ContactScreen
            self.app.switch_screen(ContactScreen())
        
        elif event.button.id == "logout":
            self.app.logout()

    def on_input_changed(self, event: Input.Changed) -> None:
        results_list_view = self.app.query_one("#results-list-view")
        results_list_view.clear()

        if event.value.strip() != "":
            response = self.api_request.search_users_by_username_request(
                search_text=event.value,
                access_token=self.app.access_token
            )
            if response["status_code"] == 200:
                for result in response["data"]["results"]:
                    results_list_view.append(ResultListItem(result["username"]))


class SearchResultContainer(Container):
    DEFAULT_CSS = SEARCH_RESULTS_CONTAINER_STYLES

    def __init__(self, results_list_view: list) -> None:
        self.results_list_view = results_list_view
        super().__init__()

    def compose(self) -> ComposeResult:
        yield self.results_list_view


class NewContactScreen(Screen):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_STYLES

    def __init__(self) -> None:
        self.results_list_view = ListView(*[], id="results-list-view")
        super().__init__()

    def compose(self) -> ComposeResult:
        yield SearchResultUpperContainer()
        yield SearchResultContainer(self.results_list_view)
 
