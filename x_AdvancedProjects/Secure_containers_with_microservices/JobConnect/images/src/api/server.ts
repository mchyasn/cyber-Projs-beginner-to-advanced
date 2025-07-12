import { homepageController } from "./controllers/homepage/homepage.controller";
import { apiErrorHandler } from "../middleware/error.middleware";
import express = require('express');
import cors = require('cors');
import {oAuthModel } from "../middleware/auth.middleware";
import { loggingService } from "../middleware/logging.middleware";
const ExpresOAuthServer = require('@node-oauth/express-oauth-server');
const path = require('path');
import {ImageController} from "./controllers/image/image.controller";
import {upload} from "./controllers/image/multer.storage";
export const server = express()
// Allow CORS for process.env.CORS_ORIGIN
server.use(cors({
    origin: process.env.CORS_ORIGIN
}))
console.log('Allowed CORS for', process.env.CORS_ORIGIN)

// Security
const auth = new ExpresOAuthServer({ model: oAuthModel });

// Middleware to parse JSON and URL-encoded data
//server.use(express.json());
//server.use(express.urlencoded({ extended: true }));

//server.use(auth.authenticate());

// Use the loggingService middleware after authentication
server.use(loggingService);

// Homepage
server.get('/', homepageController.homepage);
server.use('/uploads', express.static(path.join(__dirname,"..","..", 'uploads')));

const imageController = new ImageController();
server.get('/image/:id',imageController.getImages);
server.post('/image', upload.array('photos'),imageController.uploadImages);

server.use(apiErrorHandler);
