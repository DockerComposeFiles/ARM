"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const http_1 = require("http");
const socket_io_1 = require("socket.io");
const httpServer = http_1.createServer();
const io = new socket_io_1.Server(httpServer, {
//
});
io.on("connection", (socket) => {
    // ...
});
httpServer.listen(3000);
//# sourceMappingURL=get_data.js.map