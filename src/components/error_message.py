from textual.widgets import Static


class ErrorMessage(Static):
    DEFAULT_CSS = '''
    ErrorMessage {
        border: round darkred;
        background: darkred;
        color: white;
        content-align: center middle;
        text-style: bold;
        margin-left: 1;
        margin-right: 1;
        margin-top: 1;
        display: none;
    }
    '''
