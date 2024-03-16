from src.api_requests import ApiRequests


class TestAddNewContactRequest:
    api_request = ApiRequests()

    def test_permission_unauthorized_fail(self) -> None:
        access_token = "dummy_access_token"
        contact_username = "Username2"
        res = self.api_request.add_new_contact_request(
            contact_username=contact_username,
            access_token=access_token
        )
        assert res["status_code"] == 401

    def test_contact_not_exist_fail(self) -> None:
        # valid test access token for user (Username1)
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        contact_username = "Username233830oDummy"
        res = self.api_request.add_new_contact_request(
            contact_username=contact_username,
            access_token=access_token
        )
        assert res["status_code"] == 400
        assert res["data"]["contact_not_exist"] is True
    
    def test_add_new_contact_success(self) -> None:
        # valid test access token for user (Username1)
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        contact_username = "Username2"
        res = self.api_request.add_new_contact_request(
            contact_username=contact_username,
            access_token=access_token
        )
        assert res["status_code"] == 200
        assert res["data"]["success"] is True

