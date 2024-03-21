from textual.widgets import Input, Button, ListView
from textual.worker import get_current_worker
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import work

from components.search_result_list_item import ResultListItem
from components.header import TosChatHeader
from api_requests import ApiRequests
from styles.css import (
    NEW_CONTACT_SCREEN_STYLES,
    SEARCH_RESULTS_CONTAINER_STYLES,
    NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES,
    SEARCH_RESULTS_PAGINATION_BUTTONS_STYLE
)


class SearchResultUpperContainer(Container):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES
    api_request = ApiRequests()

    def __init__(self) -> None:
        self.search_text = ""
        super().__init__()

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
            
    async def on_input_changed(self, event: Input.Changed) -> None:
        self.search_text = event.value
        self.app.query_one("SearchResultPaginationButtons").pagination_page = 1
        self.search_user()

    @work(exclusive=True, thread=True)
    def search_user(self) -> None:
        worker = get_current_worker()
        pagination_btns = self.app.query_one("SearchResultPaginationButtons")
        results_list_view = self.app.query_one("#results-list-view")

        if not worker.is_cancelled:
            self.app.call_from_thread(results_list_view.clear)

        if self.search_text.strip() != "":
            res = self.api_request.search_users_by_username_request(
                search_text=self.search_text,
                access_token=self.app.access_token,
                page=pagination_btns.pagination_page
            )
            if res["status_code"] == 200:
                results_list_item = [ResultListItem(result["username"], result["added"]) for result in res["data"]["results"]]

                if not worker.is_cancelled:
                    self.app.call_from_thread(results_list_view.extend, results_list_item)

                # update pagination
                pagination_btns.query_one("#previous-btn").disabled = False if res["data"]["has_previous"] else True
                pagination_btns.query_one("#next-btn").disabled = False if res["data"]["has_next"] else True
                pagination_btns.query_one("#pagination-number").label = f".. {res['data']['current_page']} .."
        else: 
            item = ResultListItem("", "", empty_result=True)
            if not worker.is_cancelled:
                self.app.call_from_thread(results_list_view.append, item)


class SearchResultContainer(Container):
    DEFAULT_CSS = SEARCH_RESULTS_CONTAINER_STYLES

    def __init__(self, results_list_view: list) -> None:
        self.results_list_view = results_list_view
        super().__init__()

    def compose(self) -> ComposeResult:
        yield self.results_list_view


class SearchResultPaginationButtons(Container):
    DEFAULT_CSS = SEARCH_RESULTS_PAGINATION_BUTTONS_STYLE

    def __init__(self) -> None:
        self.pagination_page = 1
        self.api_request = ApiRequests()
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Button("< previous", id="previous-btn", disabled=True)
        yield Button(".. 1 ..", id="pagination-number", disabled=True)
        yield Button("next >", id="next-btn", disabled=True)

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        self.handle_pagination_buttons_press(event.button.id)

    @work(exclusive=True, thread=True)
    def handle_pagination_buttons_press(self, button_id: str) -> None:
        if button_id == "previous-btn":
            self.pagination_page = self.pagination_page - 1
        elif button_id == "next-btn":
            self.pagination_page = self.pagination_page + 1
        
        worker = get_current_worker()
        results_list_view = self.app.query_one("#results-list-view")

        if not worker.is_cancelled:
            self.app.call_from_thread(results_list_view.clear)

        search_text = self.app.query_one("SearchResultUpperContainer").search_text
        if search_text.strip() != "":
            res = self.api_request.search_users_by_username_request(
                search_text=search_text,
                access_token=self.app.access_token,
                page=self.pagination_page
            )
            if res["status_code"] == 200:
                results_list_item = [ResultListItem(result["username"], result["added"]) for result in res["data"]["results"]]

                if not worker.is_cancelled:
                    self.app.call_from_thread(results_list_view.extend, results_list_item)

                # update pagination
                self.query_one("#previous-btn").disabled = False if res["data"]["has_previous"] else True
                self.query_one("#next-btn").disabled = False if res["data"]["has_next"] else True
                self.query_one("#pagination-number").label = f".. {res['data']['current_page']} .."
        else: 
            item = ResultListItem("", "", empty_result=True)
            if not worker.is_cancelled:
                self.app.call_from_thread(results_list_view.append, item)

class NewContactScreen(Screen):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_STYLES

    def __init__(self) -> None:
        self.results_list_view = ListView(*[], id="results-list-view")
        super().__init__()

    def compose(self) -> ComposeResult:
        yield TosChatHeader()
        yield SearchResultUpperContainer()
        yield SearchResultContainer(self.results_list_view)
        yield SearchResultPaginationButtons()

    def on_screen_resume(self, event) -> None:
        self.results_list_view.append(
            ResultListItem("", "", empty_result=True)
        )
