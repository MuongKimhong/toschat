from typing import Dict


def get_messages() -> list[Dict[str, Dict[str, str]]]:
    messages = [
        {
            "sender": {"username": "testing", "id": "1"},
            "message": {"id": "1", "text": "Hello world"}
        },
        {
            "sender": {"username": "current", "id": "2"},
            "message": {"id": "1", "text": "Hey man"}
        },
        {
            "sender": {"username": "testing", "id": "1"},
            "message": {"id": "3", "text": "What are you doing"}
        },
    ]
    return messages