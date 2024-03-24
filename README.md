## Chat with your friends within your terminal (Linux & Mac)

Sign In             |  Let Chat!
:-------------------------:|:-------------------------:
![Screenshot](new_screenshot_one.png)   |  ![Screenshot](new_screenshot_two.png)

## Note
on Linux, if you're using Ubuntu or Debain terminal will be resize automatically when app starts. 

on MacOs, terminal will be resize automatically when app starts if you're using
iTerm, iTerm2 or Terminal.

For better experience change font size to 10 or 11

## Installation
```bash
curl -sSL https://raw.githubusercontent.com/MuongKimhong/toschat/master/install.sh | bash
```
### Usage
use `toschat` command to open the application
```bash
toschat
```
to quit the application presse `Ctrl+c` or use icoo at left of the header

All data are stored in live server!

## Contribution

You are welcome and free to contribute to the project. To do that:
- if you're doing something related to sending new data to server or make changes to servers, you might want to run servers locally for both `Django` and `Socket.io` (werbsocket) servers
- create a new python3 venv in `toschat` directory with the name of `.venv`

toschat is built on top of Textual framework (https://textual.textualize.io/)
#### Starting development process
```
$ cd toschat
$ python3 -m venv .venv && source .venv/bin/activate
$ pip3 install -r requirements.txt

# run the application for development
$ textual run --dev src/main.py
```
to see message logs, you can you textual-dev server https://textual.textualize.io/guide/devtools/#live-editing
```
$ textual console
```
#### To start Django & Socket.io servers locally
Please make sure to change server urls to local url in `src/api_requests.py` and `src/main.py`
```
$ python3 server/manage.py makemigrations
$ python3 server/manage.py migrate
$ python3 server/manage.py runserver
```
```
$ cd websocket
$ npm install
$ node index.js

# or using nodemon for live changes
$ npm start
```
