SIGN_IN_SCREEN_STYLES = '''
    SignInScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 0 6;
    }
    #sign-in-txt {
        text-style: bold;
        content-align: center middle;
        margin-top: 3;
    }
    #or-txt {
        text-style: bold;
        content-align: center middle;
    }
'''

SIGN_UP_SCREEN_STYLES = '''
    SignUpScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 0 6;
    }
    #create-new-account-txt {
        text-style: bold;
        content-align: center middle;
        margin-top: 3;
    }
    #or-txt {
        text-style: bold;
        content-align: center middle;
    }
'''

CONTACT_SCREEN_STYLES = '''
    ContactScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 0 2;
    }
'''

CONTACT_SCREEN_UPPER_CONTAINER_STYLES = '''
ContactListUpperContainer {
    align: center top;
    layout: grid;
    grid-size: 3;
    grid-columns: 3fr 1fr 1fr;
    height: 3;
    margin-top: 1;
}
#new-contact {
    margin-left: 2;
}
#logout {
    margin-right: 1;
}
'''

CONTACT_LIST_CONTAINER_STYLES= '''
    ContactListContainer {
        margin-top: 2;
        padding-left: 2;
        padding-right: 2;
    }
    ListView {
        background: rgb(18, 18, 18);
    }
'''

CONTACT_STYLES = '''
    Contact {
        align: center middle;
        layout: grid;
        grid-size: 2;
        grid-columns: 3fr 1fr;
        height: 3;
        border: round grey;
        border-left: hidden grey;
        border-right: hidden grey;
        border-top: hidden grey;
    }
    .username {
        text-style: bold;
    }
    .arrow {
        text-style: bold;
        content-align: right middle;
    }
'''

CONTACT_LIST_ITEM_STYLES = '''
    ContactListItem {
        height: 3;
        padding-top: 1;
        padding-left: 2;
        padding-right: 2;
        background: rgb(18, 18, 18);
        overflow: hidden hidden;
    }
    #empty-contact-txt {
        content-align: center middle;
        margin-top: 1;
        color: white;
    }
'''

NEW_CONTACT_SCREEN_STYLES = '''
    NewContactScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 0 2;
    }
'''


SEARCH_RESULTS_CONTAINER_STYLES = '''
    SearchResultContainer {
        margin-top: 2;
        padding-left: 2;
        padding-right: 2;
        height: 80%;
    }
    ListView {
        background: rgb(18, 18, 18);
    }
'''

RESULT_LIST_ITEM_STYLES = '''
    ResultListItem {
        height: 3;
        padding-top: 1;
        padding-left: 2;
        padding-right: 2;
        background: rgb(18, 18, 18);
        overflow: hidden hidden;
    }
    #empty-result-txt {
        content-align: center middle;
        margin-top: 1;
        color: white;
    }
'''

RESULT_STYLES = '''
    Result {
        align: center middle;
        layout: grid;
        grid-size: 2;
        grid-columns: 3fr 1fr;
        height: 3;
        border: round grey;
        border-left: hidden grey;
        border-right: hidden grey;
        border-top: hidden grey;
    }
    .username {
        text-style: bold;
    }
    .add-btn {
        content-align: right middle;
        border: none;
        height: 1;
        color: white;
    }
    .add-btn > :hover {
        border: none;
        background: $panel-darken-2;
        color: $text;
    }
'''

NEW_CONTACT_SCREEN_UPPER_CONTAINER_STYLES = '''
    SearchResultUpperContainer {
        align: center top;
        layout: grid;
        grid-size: 3;
        grid-columns: 3fr 1fr 1fr;
        height: 3;
        margin-top: 1;
    }
    #go-back-btn {
        margin-left: 2;
    }
    #logout {
        margin-right: 1;
    }
'''


CHAT_SCREEN_STYLES = '''
    ChatScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 0 2;
    }
    #back-btn {
        border: none;
        height: 1;
    }
    #write-message-input {
        border: tall grey;
    }
'''

MESSAGES_CONTAINER_STYLES = '''
    MessagesContainer {
        padding: 1 1;
        border: round grey;
        border-top: hidden grey;
        border-left: hidden grey;
        border-right: hidden grey;
        color: white;
        height: 85%;
    }
'''

SEARCH_RESULTS_PAGINATION_BUTTONS_STYLE = '''
    SearchResultPaginationButtons {
        align: center middle;
        layout: grid;
        grid-size: 3;
        grid-columns: 2fr 2fr 2fr;
        height: 1;
    }
    #previous-btn {
        border: none;
        height: 1;
        content-align: center middle;
    }
    #next-btn {
        border: none;
        height: 1;
        content-align: center middle;
    }
    #pagination-number {
        border: none;
        height: 1;
        content-align: center middle;
    }
'''