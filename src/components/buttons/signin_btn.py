from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Button

from screens.contacts import ContactScreen
from api_requests import ApiRequests


class SignInButton(Container, can_focus=True):
    DEFAULT_CSS = '''   
    SignInButton {
        margin-top: 0;
        padding-top: 0;
        align: center middle;
        width: 100%;
        height: 5;
    }
    #signin-btn {
        content-align: center middle;
        width: 4; 
    }
    '''

    def compose(self) -> ComposeResult:
        yield Button("Sign In", variant="default", id="signin-btn")

    def send_request(self) -> None:
        u_input = self.app.query_one("#signin-username-input")
        p_input = self.app.query_one("#signin-password-input")
        pls_wait_txt = self.app.query_one("#signin-pls-wait-txt")
        err_msg = self.app.query_one("#signin-error-message")
        err_msg.styles.display = "none"

        if (u_input.value.strip() == "") or (p_input.value.strip() == ""):
            pls_wait_txt.styles.display = "none"
            err_msg.update("All input fields are required")
            err_msg.styles.display = "block"
        
        else:
            res = ApiRequests().sign_in_request(
                username=u_input.value, 
                password=p_input.value
            )
            if res["status_code"] == 400:
                pls_wait_txt.styles.display = "none"
                err_msg.update("Username or password is incorrect")
                err_msg.styles.display = "block"
                u_input.focus()
            elif res["status_code"] == 200:
                self.app.access_token = res["data"]["access_token"]
                self.app.user = res["data"]["user"]

                if len(res["data"]["user"]["username"]) < 15: 
                    self.app.title = f"Signed in as {res['data']['user']['username']}"
                else:
                    self.app.title = res["data"]["user"]["username"]

                self.app.switch_screen(ContactScreen())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.query_one("#signin-error-message").styles.display = "none"
        self.app.query_one("#signin-pls-wait-txt").styles.display = "block"
        self.app.set_timer(delay=0.1, callback=self.send_request)
