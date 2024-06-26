from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Button
from textual import events

from api_requests import ApiRequests


class SignUpButton(Container, can_focus=True):
    DEFAULT_CSS = '''   
    SignUpButton {
        margin-top: 0;
        padding-top: 0;
        align: center middle;
        width: 100%;
        height: 5;
    }
    #signup-btn {
        content-align: center middle;
        width: 4; 
    }
    '''

    def compose(self) -> ComposeResult:
        yield Button("Sign Up", variant="default", id="signup-btn")

    def send_request(self) -> None:
        u_input = self.app.query_one("#signup-username-input")
        p_input = self.app.query_one("#signup-password-input")
        c_p_input = self.app.query_one("#signup-confirm-password-input")
        pls_wait_text = self.app.query_one("#signup-pls-wait-txt")
        err_msg = self.app.query_one("#signup-error-message")
        err_msg.styles.display = "none"

        if (u_input.value.strip() == "") or (p_input.value.strip() == "") or (c_p_input.value.strip() == ""):
            pls_wait_text.styles.display = "none"
            err_msg.update("All input fields are required")
            err_msg.styles.display = "block"
        
        else:
            res = ApiRequests().sign_up_request(
                username=u_input.value, 
                password=p_input.value, 
                confirm_password=c_p_input.value
            )

            if res["status_code"] == 400:
                if "password_length_err" in res["data"]:
                    err_msg.update(res["data"]["password_length_err"])

                elif "password_not_match" in res["data"]:
                    err_msg.update(res["data"]["password_not_match"])

                elif "username_taken" in res["data"]:
                    err_msg.update(res["data"]["username_taken"])

                pls_wait_text.styles.display = "none"
                err_msg.styles.display = "block"
                u_input.focus()
            else:
                from screens.sign_in import SignInScreen
                self.app.switch_screen(SignInScreen())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.query_one("#signup-error-message").styles.display = "none"
        self.app.query_one("#signup-pls-wait-txt").styles.display = "block"
        self.app.set_timer(delay=0.1, callback=self.send_request)

    def on_focus(self, event: events.Focus) -> None:
        # forward focus to signup button immediately
        self.query_one("#signup-btn").focus() 