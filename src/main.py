from textual.app import App
from textual import events, work, log

from custom_messages_events import ReceiveOnlineStatusUpdate
from screens.contacts import ContactScreen
from screens.sign_in import SignInScreen
from api_requests import ApiRequests
import socketio


class Main(App):
    def __init__(self) -> None:
        self.access_token: str | None = None
        self.current_chatroom_id: int | None = None
        self.current_chat_username: str | None = None
        self.user: dict = dict()

        # handle user online status update (online or offline)
        self.websocket_online_status_namespace = None
        self.registered_atexit_handler = False

        self.websocket_url = "https://websockethandler.toschat.xyz"
        super().__init__()

    def logout(self) -> None:
        self.handle_user_goes_offline_request()
        self.websocket_online_status_namespace.emit(
            "update-online-status",
            {"sender_name": self.app.user["username"], "status": "offline"},
            namespace="/onlineStatus"
        )
        self.title = "TosChat"
        self.access_token = None
        self.current_chatroom_id = None
        self.current_chat_username = None
        self.user = None
        self.switch_screen(SignInScreen())

    @work(exclusive=True, thread=True)
    def handle_user_goes_offline_request(self) -> None:
        if self.access_token is not None:
            res = ApiRequests().user_goes_offline_request(self.access_token)

    def connect_websocket_online_status_namespace(self) -> None:
        self.websocket_online_status_namespace = socketio.Client()
        self.websocket_online_status_namespace.connect(
            self.websocket_url, 
            namespaces=['/onlineStatus']
        )
        
        @self.websocket_online_status_namespace.on("online-status-update", namespace="/onlineStatus")
        def on_message(update_data: dict):
            self.listen_websocket_online_status_namespace(
                update_data=update_data
            )
    
    def listen_websocket_online_status_namespace(self, update_data: dict) -> None:
        self.post_message(
            ReceiveOnlineStatusUpdate(update_data)
        )

    def on_receive_online_status_update(self, update_event: ReceiveOnlineStatusUpdate) -> None: 
        # current active screen
        if self.screen.screen_name == "ContactScreen":
            update_data = update_event.update_data

            if update_data['sender_name'] != self.app.user.get("username"):
                contact_username = self.query_one(f"#contact-{update_data['sender_name']}")

                if update_data["status"] == "online":
                    contact_username.update(
                        renderable=f"{update_data['sender_name']} (online)"
                    )
                    contact_username.styles.color = "greenyellow"
                else:
                    contact_username.update(
                        renderable=update_data['sender_name']
                    )
                    contact_username.styles.color = "white"

    def on_mount(self, event: events.Mount) -> None:
        self.push_screen(SignInScreen()) # default screen
        self.title = "TosChat" # header text


if __name__ == "__main__":
    app = Main()
    app.run()
