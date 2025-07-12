import { Server } from "socket.io";
import * as http from "node:http";

let io = null;

export const socketServer = {
    init(httpServer: http.Server) {
        io = new Server(httpServer, {
            cors: {
                origin: process.env.CORS_ORIGIN.split(","),
            },
        });

        io.on("connection", (socket) => {
            console.log("Socket.io: A new user " + socket.id + " connected");

            socket.on("joinRoom", (itemId: string) => {
                console.log(`Socket.io: User ${socket.id} joined room ${itemId}`);
                socket.join(itemId);
            });

            socket.on("message", ({ itemId, message }) => {
                console.log(`Socket.io: Message received in room ${itemId}`, message);

                io.to(itemId).emit("message", {
                    sender: socket.id,
                    message,
                });
            });

            socket.on("disconnect", () => {
                console.log("Socket.io: User " + socket.id + " disconnected");
            });
        });

        console.log("Socket.io: Initialized");
    },
};
