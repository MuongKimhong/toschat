import socketio
import time

def test_connect_websocket():
    sio = socketio.Client()
    sio.connect("https://websockethandler.toschat.xyz")


