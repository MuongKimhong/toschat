from typing import Dict, Union
from textual.message import Message


class ReceiveNewChatMessage(Message):
    def __init__(self, new_message: Dict[str, Union[int, dict]]) -> None:
        self.new_message = new_message
        super().__init__()
