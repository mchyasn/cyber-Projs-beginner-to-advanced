import 'reflect-metadata';
import { server } from './api/server';
import { Config } from "../config";
import {createServer} from 'http';

const port = Config.port || 3000;
const httpServer = createServer(server);

async function init() {

    httpServer.listen(port, () => {
        console.log(`Listening on http://localhost:${port}`);
    });
}

init();