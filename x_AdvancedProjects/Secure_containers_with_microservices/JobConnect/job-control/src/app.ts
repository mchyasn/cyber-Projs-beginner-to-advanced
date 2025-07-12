import 'reflect-metadata';
import { server } from './api/server';
import mongo from "./persistence/mongo";
import { Config } from "../config";
import {createServer} from 'http';

const port = Config.port || 3000;
const httpServer = createServer(server);

async function init() {
    await mongo.connect();

    httpServer.listen(port, () => {
        console.log(`Listening on http://localhost:${port}`);
    });
}

init();