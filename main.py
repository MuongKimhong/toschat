from textual.app import App
from textual import events


class Main(App):
    def __init__(self) -> None:
        super().__init__()

    def on_mount(self, event: events.Mount) -> None:
        pass


if __name__ == "__main__":
    app = Main()
    app.run()
