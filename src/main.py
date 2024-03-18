from textual.app import App
from textual import events

from screens.sign_in import SignInScreen


class Main(App):
    def __init__(self) -> None:
        self.access_token: str | None = None
        self.current_chatroom_id: int | None = None
        self.user: dict = dict()
        super().__init__()

    def logout(self) -> None:
        self.access_token = None
        self.current_chatroom_id = None
        self.user = None
        self.switch_screen(SignInScreen())

    def on_mount(self, event: events.Mount) -> None:
        # default screen
        self.push_screen(SignInScreen())


if __name__ == "__main__":
    app = Main()
    app.run()
