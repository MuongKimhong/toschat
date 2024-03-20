from textual.widgets import Input
from textual import events


from custom_messages_events import ReceiveNewChatMessage
from api_requests import ApiRequests


class WriteMessageInput(Input, can_focus=True):
    DEFAULT_CSS = '''
    WriteMessageInput {
        color: white;
    }
    WriteMessageInput:focus {
        border: tall rgb(40, 40, 40);
    }
    WriteMessageInput>.input--cursor {
        background: $surface;
        color: $text;
        text-style: reverse;
    }
    '''

    def on_mount(self, event: events.Mount) -> None:
        self.focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        message = event.value.strip()

        if message != "":
            res = ApiRequests().send_message_request(
                chatroom_id=self.app.current_chatroom_id,
                text=message,
                access_token=self.app.access_token
            )
            if res["status_code"] == 200:
                chatscreen = self.app.query_one("ChatScreen")
                chatscreen.websocket.emit("send-message", res["data"]["new_message"])
                self.app.set_timer(delay=0.1, callback=chatscreen.messages_list_view.scroll_end)
                chatscreen.post_message(
                    ReceiveNewChatMessage(res["data"]["new_message"])
                )

            self.value = ""