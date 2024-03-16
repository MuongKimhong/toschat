from src.api_requests import ApiRequests


class TestSignInRequest:
    api_request = ApiRequests()

    def test_username_fail(self) -> None:
        username = "DummyUser"
        password = "12345678"
        res = self.api_request.sign_in_request(
            username=username,
            password=password
        )
        assert res["status_code"] == 400
        assert res["data"]["error"] is True

    def test_password_fail(self) -> None:
        username = "Username1"
        password = "dummypassword"
        res = self.api_request.sign_in_request(
            username=username,
            password=password
        )
        assert res["status_code"] == 400
        assert res["data"]["error"] is True

    def test_sign_in_success(self) -> None:
        username = "Username1"
        password = "123456789"
        res = self.api_request.sign_in_request(
            username=username,
            password=password
        )
        assert res["status_code"] == 200
        assert "user" in res["data"]
