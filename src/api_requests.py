from typing import Dict, Union
import requests


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


class ApiRequests:
    def __init__(self) -> None:
        self.base_url = "http://localhost:8000/"

    def sign_up_request(self, username: str, password: str, confirm_password: str):
        url = f"{self.base_url}/api-account/sign-up/" 
        data = {
            "username": username,
            "password": password,
            "confirm_password": confirm_password
        }
        res = requests.post(url, data)
        return {"status_code": res.status_code, "data": res.json()}

    def sign_in_request(self, username: str, password: str):
        url = f"{self.base_url}/api-account/sign-in/"
        data = {"username": username, "password": password}
        res = requests.post(url, data)
        return {"status_code": res.status_code, "data": res.json()}

    def get_all_contacts_request(self, access_token: str):
        url = f"{self.base_url}/api-account/get-all-contacts/"
        res = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
        return {"status_code": res.status_code, "data": res.json()}

    def add_new_contact_request(self, contact_username: str, access_token: str):
        url = f"{self.base_url}/api-account/add-new-contact/"
        data = {"contact_username": contact_username} 
        res = requests.post(url, data=data, headers={"Authorization": f"Bearer {access_token}"})
        return {"status_code": res.status_code, "data": res.json()}

    def search_contacts_request(self, search_text: str, access_token: str):
        url = f"{self.base_url}/api-account/search-contact/"
        params = {"search_text": search_text}
        res = requests.get(url, params=params, headers={"Authorization": f"Bearer {access_token}"})
        return {"status_code": res.status_code, "data": res.json()} 

    def search_users_by_username_request(self, search_text: str, access_token: str):
        url = f"{self.base_url}/api-account/search-users-by-username/"
        params = {"search_text": search_text}
        res = requests.get(url, params=params, headers={"Authorization": f"Bearer {access_token}"})
        return {"status_code": res.status_code, "data": res.json()}        

    def get_messages_request(self, chatroom_id: int, access_token: str):
        url = f"{self.base_url}/api-chat/get-messages/"
        params = {"chatroom_id": chatroom__id}
        res = requests.get(url, params=params, headers={"Authorization": f"Bearer {access_token}"})
        return {"status_code": res.status_code, "data": res.json()} 

    def send_message_request(self, chatroom_id: int, text: str, access_token: str):
        url = f"{self.base_url}/api-chat/send-message/"
        data = {"chatroom_id": chatroom_id, "text": text}
        res = requests.get(url, data=data, headers={"Authorization": f"Bearer {access_token}"})
        return {"status_code": res.status_code, "data": res.json()}  
