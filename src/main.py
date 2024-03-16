from typing import Dict

from textual.app import App
from textual import events, log

from screens.sign_in import SignInScreen
from screens.sign_up import SignUpScreen


class Main(App):
    def __init__(self) -> None:
        self.access_token: str | None = None
        self.current_chatroom_id: int | None = None
        self.user: Dict[str, str] = dict()
        super().__init__()

    def on_mount(self, event: events.Mount) -> None:
        self.push_screen(SignUpScreen())


if __name__ == "__main__":
    app = Main()
    app.run()
