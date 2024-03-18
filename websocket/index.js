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

socketIO.on("connection", (socket) => {
    socket.on("send-message", (message) => {
        socket.broadcast.emit("new-message", message);
    })
})