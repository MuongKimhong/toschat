const express = require("express");
const cors = require("cors");
const app = express();
const server = require("http").createServer(app);
const socketIO = require("socket.io")(server)

const devPort = 3000;

app.use(cors("*")); // enable cors for all origins
app.use(express.json()); // tell server to accept json format

server.listen(devPort, () => {
    console.log("websocket server started");
})

// default namespace "/" for handling chat message
socketIO.on("connection", (socket) => {
    socket.on("send-message", (message) => {
        socket.broadcast.emit("new-message", message);
    })
})

// namespace "/onlineStatus" for handling user online & offline status
const onlineStatus = socketIO.of("/onlineStatus");
onlineStatus.on("connection", (socket) => {
    socket.on("update-online-status", (data) => {
        // data content : {sender_name: "somename", status: "online"}
        // data content : {sender_name: "somename", status: "offline"}
        socket.broadcast.emit("online-status-update", data);
    })
})
