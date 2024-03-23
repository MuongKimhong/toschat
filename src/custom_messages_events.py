from typing import Dict
from textual.message import Message


class ReceiveNewChatMessage(Message):
    def __init__(self, new_message: Dict[str, int | dict]) -> None:
        self.new_message = new_message
        super().__init__()


class ReceiveOnlineStatusUpdate(Message):
    def __init__(self, update_data: dict) -> None:
        self.update_data = update_data
        super().__init__()
