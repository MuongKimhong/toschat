from textual.widgets import Header, Static


class TosChatHeader(Header):
    DEFAULT_CSS = '''
    TosChatHeader {
        background: $panel;
        color: white;
        text-style: bold;
    }
    '''

    def __init__(self) -> None:
        super().__init__(show_clock=True)
