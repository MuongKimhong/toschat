SIGN_IN_SCREEN_STYLES = '''
    SignInScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 3 6;
    }
    #sign-in-txt {
        text-style: bold;
        content-align: center middle
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
        padding: 3 6;
    }
    #create-new-account-txt {
        text-style: bold;
        content-align: center middle;
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
        padding: 1 2;
    }
'''

CONTACT_SCREEN_UPPER_CONTAINER_STYLES = '''
ContactListUpperContainer {
    align: center top;
    layout: grid;
    grid-size: 2;
    grid-columns: 3fr 1fr;
    height: 3;
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
'''

NEW_CONTACT_SCREEN_STYLES = '''
    NewContactScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 1 2;
    }
'''


SEARCH_RESULTS_CONTAINER_STYLES = '''
    SearchResultContainer {
        margin-top: 2;
        padding-left: 2;
        padding-right: 2;
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
        grid-size: 2;
        grid-columns: 3fr 1fr;
        height: 3;
    }
'''


CHAT_SCREEN_STYLES = '''
    ChatScreen {
        background: rgb(18, 18, 18);
        color: white;
        padding: 1 2;
    }
'''