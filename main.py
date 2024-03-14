from textual.app import App
from textual import events, log

from screens.sign_in import SignInScreen

# import screens to test
from screens.contacts import ContactScreen


class Main(App):
    def __init__(self) -> None:
        super().__init__()

    def on_mount(self, event: events.Mount) -> None:
        self.push_screen(ContactScreen())


if __name__ == "__main__":
    app = Main()
    app.run()
