from textual.app import App
from textual import events, log

from screens.sign_in import SignInScreen


class Main(App):
    def __init__(self) -> None:
        super().__init__()

    def on_mount(self, event: events.Mount) -> None:
        self.push_screen(SignInScreen())


if __name__ == "__main__":
    app = Main()
    app.run()
