import 'reflect-metadata';
import { Config } from "../config";
import { socketServer } from "./socket/socket.server";
import {createServer} from 'http';
import express = require('express');

export const server = express()
const port = Config.port || 3001;
const httpServer = createServer(server);

async function init() {

    httpServer.listen(port, () => {
        console.log(`Listening on http://localhost:${port}`);
    });

    socketServer.init(httpServer);
}

init();