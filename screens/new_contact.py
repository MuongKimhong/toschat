from textual.widgets import Input, Button, ListView, ListItem, Static
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, log

from styles.css import NEW_CONTACT_SCREEN_STYLES


class SearchResultContainer(Container):
    DEFAULT_CSS = '''
        SearchResultContainer {
            margin-top: 2;
            padding-left: 2;
            padding-right: 2;
        }
        ListView {
            background: rgb(18, 18, 18);
        }
        ListItem {
            background: rgb(18, 18, 18);
            height: 3;
            padding-top: 1;
        }
        Static {
            height: 3;
        }
    '''

    def compose(self) -> ComposeResult:
        results = [ListItem(Static(f"username{i + 1}")) for i in range(10)]
        yield ListView(*results)


class NewContactScreen(Screen):
    DEFAULT_CSS = NEW_CONTACT_SCREEN_STYLES

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter contact name to search")
        yield SearchResultContainer()
