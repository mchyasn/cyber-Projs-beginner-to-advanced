import { io, Socket } from "socket.io-client";
import Config from "@/config";

export function useChatService() {
    let socket: Socket | null = null;

    async function init() {
        socket = io(Config.chatBackend);

        socket.on("disconnect", () => {
            console.log("Socket.io: disconnected");
        });

        return new Promise<void>((resolve) => {
            socket?.on("connect", () => {
                console.log("Socket.io: connected");
                resolve();
            });
        });
    }

    function joinRoom(itemId: string) {
        console.log(`Socket.io: Joining room ${itemId}`);
        socket?.emit("joinRoom", itemId);
    }

    function sendMessage(itemId: string, message: string) {
        console.log(`Socket.io: Sending message to room ${itemId}`, message);
        socket?.emit("message", { itemId, message });
    }

    function onMessage(callback: (data: { sender: string; message: string }) => void) {
        socket?.on("message", callback);
    }

    function getClientId(): string | undefined {
        if (socket) {
            return socket.id;
        }
        console.warn("Socket.io: Socket not initialized. Call init() first.");
        return undefined;
    }

    function disconnect() {
        socket?.disconnect();
    }

    return {
        init,
        joinRoom,
        sendMessage,
        onMessage,
        getClientId,
        disconnect,
    };
}
