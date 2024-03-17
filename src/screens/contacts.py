from textual.widgets import Static, Button, Input, Label
from textual.widgets import ListView, ListItem
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from components.contact_list_item import ContactListItem
from api_requests import ApiRequests
from styles.css import (
    CONTACT_SCREEN_STYLES,
    CONTACT_LIST_CONTAINER_STYLES,
    CONTACT_SCREEN_UPPER_CONTAINER_STYLES
)


class ContactListUpperContainer(Container):
    DEFAULT_CSS = CONTACT_SCREEN_UPPER_CONTAINER_STYLES

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Search contacts")
        yield Button("New", variant="default", id="new-contact")
        yield Button("Logout", variant="default", id="logout")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "new-contact":
            from screens.new_contact import NewContactScreen
            self.app.switch_screen(NewContactScreen())
        
        elif event.button.id == "logout":
            self.app.logout()

    def on_input_changed(self, event: Input.Changed) -> None:
        contacts_list_view = self.app.query_one("#contacts-list-view")
        contacts_list_view.clear()

        if event.value.strip() == "":
            res = ApiRequests().get_all_contacts_request(self.app.access_token)

            for contact in res["data"]["contacts"]:
                contacts_list_view.append(
                    ContactListItem(contact["username"])
                )        
        else:
            res = ApiRequests().search_contacts_request(
                search_text=event.value,
                access_token=self.app.access_token
            )
            for result in res["data"]["results"]:
                contacts_list_view.append(
                    ContactListItem(result["username"])
                )


class ContactListContainer(Container):
    DEFAULT_CSS = CONTACT_LIST_CONTAINER_STYLES

    def __init__(self, contacts_list_view: ListView) -> None:
        self.contacts_list_view = contacts_list_view
        super().__init__()

    def compose(self) -> ComposeResult:
        yield self.contacts_list_view


class ContactScreen(Screen, can_focus=True):
    DEFAULT_CSS = CONTACT_SCREEN_STYLES
    contacts = list()

    def __init__(self) -> None:
        self.contacts_list_view = ListView(*[], id="contacts-list-view")
        super().__init__()

    def compose(self) -> ComposeResult:
        yield ContactListUpperContainer()
        yield ContactListContainer(contacts_list_view=self.contacts_list_view)

    def on_screen_resume(self, event: events.ScreenResume) -> None:
        self.contacts_list_view.clear()
        res = ApiRequests().get_all_contacts_request(self.app.access_token)

        if res["status_code"] == 200:
            for contact in res["data"]["contacts"]:
                self.contacts_list_view.append(
                    ContactListItem(contact["username"])
                )
