from src.api_requests import ApiRequests


class TestSignUpRequest:
    api_request = ApiRequests()

    def test_password_length_fail(self) -> None:
        username = "TestingName1"
        password = "12345"
        res = self.api_request.sign_up_request(
            username=username,
            password=password,
            confirm_password=password
        )
        assert res["status_code"] == 400
        assert "password_length_err" in res["data"]

    def test_two_passwords_not_match_fail(self) -> None:
        username = "TestingName1"
        password = "12345678"
        confirm_password = "12345679"
        res = self.api_request.sign_up_request(
            username=username,
            password=password,
            confirm_password=confirm_password
        )
        assert res["status_code"] == 400
        assert "password_not_match" in res["data"]

    def test_username_taken_fail(self) -> None:
        username = "Username1" # created dummy user
        password = "12345678"
        res = self.api_request.sign_up_request(
            username=username,
            password=password,
            confirm_password=password
        )
        assert res["status_code"] == 400
        assert "username_taken" in res["data"]

    def test_sign_up_success(self) -> None:
        username = "TestingName1"
        password = "iamsuperhero"
        res = self.api_request.sign_up_request(
            username=username, 
            password=password, 
            confirm_password=password
        )
        assert res["status_code"] == 200
        assert res["data"]["success"] is True
