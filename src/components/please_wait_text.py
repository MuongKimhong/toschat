from textual.widgets import Static


class PleaseWaitText(Static):
    DEFAULT_CSS = '''
    PleaseWaitText {
        border: round $panel;
        background: $panel;
        color: white;
        content-align: center middle;
        text-style: bold;
        margin-left: 1;
        margin-right: 1;
        margin-top: 1;
        display: none;
    }
    '''