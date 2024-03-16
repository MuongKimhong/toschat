from src.api_requests import ApiRequests


class TestGetAllContactsRequest:
    api_request = ApiRequests()

    def test_permission_unauthorized_fail(self) -> None:
        access_token = "dummy_access_token"
        res = self.api_request.get_all_contacts_request(
            access_token=access_token
        )
        assert res["status_code"] == 401

    def test_get_all_contacts_success(self) -> None:
        # valid test access token for user (Username1)
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        res = self.api_request.get_all_contacts_request(
            access_token=access_token
        )
        assert res["status_code"] == 200
        assert "contacts" in res["data"]

