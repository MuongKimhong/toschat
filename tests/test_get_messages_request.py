from src.api_requests import ApiRequests


class TestGetMessagesRequest:
    api_request = ApiRequests()

    def test_permission_unauthorized_fail(self) -> None:
        access_token = "dummy_access_token"
        chatroom_id = 3
        res = self.api_request.get_messages_request(
            chatroom_id=chatroom_id,
            access_token=access_token
        )
        assert res["status_code"] == 401

    def test_chatroom_not_exist(self) -> None:
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        chatroom_id = 33948 # dummy id
        res = self.api_request.get_messages_request(
            chatroom_id=chatroom_id,
            access_token=access_token
        )
        assert res["status_code"] == 400
        assert res["data"]["chatroom_not_exist"] is True

    def test_user_not_in_room(self) -> None:
        # access token for user (Username7)
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTc1ODA0LCJpYXQiOjE3MTA1ODM4MDQsImp0aSI6ImM1ZDk5YjMyZDlkYTQ3Yjc5ZDg5YTY5NDIxYzUzOWNhIiwidXNlcl9pZCI6N30.qb8J3cP2mfLQP8zK9Orl7XGwRsrpv1ZaqhRhVmkmg-s"
        chatroom_id = 3
        res = self.api_request.get_messages_request(
            chatroom_id=chatroom_id,
            access_token=access_token
        )
        assert res["status_code"] == 400
        assert res["data"]["user_not_in_room"] is True

    def test_get_messages_success(self) -> None:
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        chatroom_id = 3
        res = self.api_request.get_messages_request(
            chatroom_id=chatroom_id,
            access_token=access_token
        )
        assert res["status_code"] == 200
        assert "messages" in res["data"]
