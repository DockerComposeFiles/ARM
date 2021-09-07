"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const http_1 = require("http");
const socket_io_1 = require("socket.io");
const httpServer = http_1.createServer();
const io = new socket_io_1.Server(httpServer, {
//
});
io.on("connection", (socket) => {
    console.log("IN FUNCTION: io.on(connection)");
    socket.on('disconnect', function () {
        console.log("Verbindung geschlossen");
    });
});
httpServer.listen(3000);
console.log("get_data.js success");
//# sourceMappingURL=get_data.js.map