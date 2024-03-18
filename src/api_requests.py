from typing import Dict
import requests


class ApiRequests:
    def __init__(self) -> None:
        self.base_url = "http://localhost:8000/"
    
    def headers(self, access_token: str) -> Dict[str, str]:
        return {"Authorization": f"Bearer {access_token}"}

    def response(self, res) -> Dict[str, int | dict]:
        return {"status_code": res.status_code, "data": res.json()}

    def sign_up_request(self, username: str, password: str, confirm_password: str):
        url = f"{self.base_url}/api-account/sign-up/" 
        data = {
            "username": username,
            "password": password,
            "confirm_password": confirm_password
        }
        res = requests.post(url, data)
        return self.response(res)

    def sign_in_request(self, username: str, password: str):
        url = f"{self.base_url}/api-account/sign-in/"
        data = {
            "username": username, 
            "password": password
        }
        res = requests.post(url, data)
        return self.response(res)

    def get_all_contacts_request(self, access_token: str):
        url = f"{self.base_url}/api-account/get-all-contacts/"
        res = requests.get(url, headers=self.headers(access_token))
        return self.response(res)

    def add_new_contact_request(self, contact_username: str, access_token: str):
        url = f"{self.base_url}/api-account/add-new-contact/"
        data = {
            "contact_username": contact_username
        } 
        res = requests.post(url, data=data, headers=self.headers(access_token))
        return self.response(res)

    def search_contacts_request(self, search_text: str | None, access_token: str):
        url = f"{self.base_url}/api-account/search-contacts/"
        params = {
            "search_text": search_text
        }
        res = requests.get(url, params=params, headers=self.headers(access_token))
        return self.response(res)

    def search_users_by_username_request(self, search_text: str | None, access_token: str):
        url = f"{self.base_url}/api-account/search-users-by-username/"
        params = {
            "search_text": search_text
        }
        res = requests.get(url, params=params, headers=self.headers(access_token))
        return self.response(res)

    def get_messages_request(self, chatroom_id: int, access_token: str):
        url = f"{self.base_url}/api-chat/get-messages/"
        params = {
            "chatroom_id": chatroom_id
        }
        res = requests.get(url, params=params, headers=self.headers(access_token))
        return self.response(res)

    def send_message_request(self, chatroom_id: int, text: str, access_token: str):
        url = f"{self.base_url}/api-chat/send-message/"
        data = {
            "chatroom_id": chatroom_id, 
            "text": text
        }
        res = requests.post(url, data=data, headers=self.headers(access_token))
        return self.response(res)
