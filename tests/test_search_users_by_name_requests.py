from src.api_requests import ApiRequests


class TestSearchUsersByUsernameRequest:
    api_request = ApiRequests()

    def test_permission_unauthorized_fail(self) -> None:
        access_token = "dummy_access_token"
        search_text = "some_search"
        res = self.api_request.search_users_by_username_request(
            search_text=search_text,
            access_token=access_token
        )
        assert res["status_code"] == 401

    def test_param_missing_fail(self) -> None:
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        res = self.api_request.search_users_by_username_request(
            search_text=None,
            access_token=access_token
        )
        assert res["status_code"] == 400
        assert "param_missing" in res["data"]

    def test_search_users_by_username_success(self) -> None:
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTQ4MTkwLCJpYXQiOjE3MTA1NTYxOTAsImp0aSI6ImFmMmEwMzIwMGIwNDQ3NDI4ZmFhYjU2OGU2MDQ1YWRlIiwidXNlcl9pZCI6MX0.wrM19BtMxSUFo55ducdsE1JxTkGJka-zg7Nonulb1L0"
        search_texts = ["Us", "User", "Tes"] 
        
        for search_text in search_texts:
            res = self.api_request.search_users_by_username_request(
                search_text=search_text,
                access_token=access_token
            )
            assert res["status_code"] == 200
            assert "results" in res["data"]
