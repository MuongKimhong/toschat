from textual.app import App
from textual import events

from screens.sign_in import SignInScreen
from api_requests import ApiRequests

import threading
import atexit


class Main(App):
    def __init__(self) -> None:
        self.access_token: str | None = None
        self.current_chatroom_id: int | None = None
        self.current_chat_username: str | None = None
        self.user: dict = dict()
        super().__init__()

    def logout(self) -> None:
        self.access_token = None
        self.current_chatroom_id = None
        self.current_chat_username = None
        self.user = None
        self.title = "TosChat"
        self.switch_screen(SignInScreen())

    def on_mount(self, event: events.Mount) -> None:
        self.push_screen(SignInScreen()) # default screen
        self.title = "TosChat" # header text


if __name__ == "__main__":
    app = Main()
    access_token = app.access_token
    api_requests = ApiRequests()

    def app_exit_handler() -> None:
        if access_token is not None:
            thread = threading.Thread(target=user_goes_offline)
            thread.start()

        print("[INFO] Have a nice day!")

    def user_goes_offline() -> None:
        api_requests.user_goes_offline_request(access_token=access_token)

    atexit.register(app_exit_handler)
    app.run()
