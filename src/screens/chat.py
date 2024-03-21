from textual.widgets import Button, ListView, ListItem
from textual.worker import get_current_worker
from textual.containers import Container
from textual.app import ComposeResult
from textual.screen import Screen
from textual import events, work
import socketio

from components.inputs.write_message_input import WriteMessageInput
from components.header import TosChatHeader
from components.message import Message
from styles.css import CHAT_SCREEN_STYLES, MESSAGES_CONTAINER_STYLES

from custom_messages_events import ReceiveNewChatMessage
from api_requests import ApiRequests


from textual import log
import time


class ChatScreenUpperContainer(Container):
    DEFAULT_CSS = '''
        ChatScreenUpperContainer {
            align: center top;
            layout: grid;
            grid-size: 3;
            grid-columns: 2fr 2fr 2fr;
            height: 1;
            margin-top: 1;
        }
        #go-back-btn {
            border: none;
            height: 1;
            content-align: center middle;
        }
        #logout {
            border: none;
            height: 1;
            content-align: center middle;
        }
        #name-text {
            border: none;
            height: 1;
            content-align: center middle
        }
    '''

    def compose(self) -> ComposeResult:
        yield Button("< Back", variant="default", id="go-back-btn")
        yield Button(self.app.current_chat_username, variant="default", id="name-text", disabled=True)
        yield Button("Logout", variant="default", id="logout")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-back-btn":
            from screens.contacts import ContactScreen
            self.app.switch_screen(ContactScreen())
        
        elif event.button.id == "logout":
            self.app.logout()


class MessagesContainer(Container):
    DEFAULT_CSS = MESSAGES_CONTAINER_STYLES

    def __init__(self, messages_list_view: ListView) -> None:
        self.messages_list_view = messages_list_view
        super().__init__()

    def compose(self) -> ComposeResult:
        yield self.messages_list_view


class ChatScreen(Screen):
    DEFAULT_CSS = CHAT_SCREEN_STYLES

    def __init__(self) -> None:
        self.messages_list_view = ListView(*[], id="messages-list-view")
        self.websocket = None
        super().__init__()

    def compose(self) -> ComposeResult:
        yield TosChatHeader()
        yield ChatScreenUpperContainer()
        yield MessagesContainer(messages_list_view=self.messages_list_view)
        yield WriteMessageInput(placeholder="Write message")

    def connect_websocket(self) -> None:
        self.websocket = socketio.Client()
        self.websocket.connect("https://websockethandler.toschat.xyz")

        @self.websocket.on("new-message")
        def on_message(new_message):
            self.listen_websocket(new_message)

    def listen_websocket(self, new_message) -> None:
        self.post_message(ReceiveNewChatMessage(new_message))

    async def on_screen_resume(self, event: events.ScreenResume) -> None: 
        self.handle_get_message_request()
        self.connect_websocket()

    @work(exclusive=True, thread=True)
    def handle_get_message_request(self) -> None:
        worker = get_current_worker()

        res = ApiRequests().get_messages_request(
            chatroom_id=self.app.current_chatroom_id,
            access_token=self.app.access_token
        )
        if res["status_code"] == 200: 
            messages = [ListItem(Message(message)) for message in res["data"]["messages"]]
            
            if not worker.is_cancelled:
                self.app.call_from_thread(self.messages_list_view.extend, messages)
                self.app.call_from_thread(self.messages_list_view.scroll_end, animate=False)

    def on_screen_suspend(self, event) -> None:
        self.websocket.disconnect()
        self.messages_list_view.clear()

    def on_receive_new_chat_message(self, message: ReceiveNewChatMessage) -> None:
        sender = message.new_message["sender"]
        receiver = message.new_message["receiver"]
        chatroom_id = message.new_message["chatroom_id"]

        if (sender["id"] == self.app.user["id"]) or (receiver["id"] == self.app.user["id"]):
            if chatroom_id == self.app.current_chatroom_id:
                self.messages_list_view.append(ListItem(Message(message.new_message)))
                self.messages_list_view.scroll_end()
        