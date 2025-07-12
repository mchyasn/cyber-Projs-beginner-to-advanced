import { homepageController } from "./controllers/homepage/homepage.controller";
import { apiErrorHandler } from "../middleware/error.middleware";
import express = require('express');
import cors = require('cors');
import { hasAnyRole, oAuthModel } from "../middleware/auth.middleware";
import { JobController } from "./controllers/job/job.controller";
import { loggingService } from "../middleware/logging.middleware";
import {CategoryController} from "./controllers/category/category.controller";
const ExpresOAuthServer = require('@node-oauth/express-oauth-server');
import YAML from 'yamljs';
import swaggerUi from 'swagger-ui-express';
const path = require('path');

const openapiSpec = YAML.load(path.join(__dirname, 'openapi.yaml'));
export const server = express()

// Allow CORS for process.env.CORS_ORIGIN
server.use(cors({
    origin: process.env.CORS_ORIGIN
}))
console.log('Allowed CORS for', process.env.CORS_ORIGIN)

// Security
const auth = new ExpresOAuthServer({ model: oAuthModel });

// Middleware to parse JSON and URL-encoded data
server.use(express.json());
server.use(express.urlencoded({ extended: true }));
server.use('/api-docs', swaggerUi.serve, swaggerUi.setup(openapiSpec));
// Security: Authentication middleware
server.get('/', homepageController.homepage);
server.use(auth.authenticate()); // Ensure authentication happens first

// Use the loggingService middleware after authentication
server.use(loggingService);

// Homepage

// Job routes
const jobController = new JobController();
const categoryController = new CategoryController();

server.get('/categories', [hasAnyRole("CUSTOMER")], categoryController.getAll);
server.post('/categories', [hasAnyRole("CUSTOMER")], categoryController.getSubcategories);
server.get('/jobs/company', [hasAnyRole("COMPANY")], jobController.getByCompany);
server.get('/jobs/customer', [hasAnyRole("CUSTOMER")], jobController.getByCustomer);
server.post('/jobs', [hasAnyRole("CUSTOMER")], jobController.create);
server.get('/jobs', [hasAnyRole("COMPANY")], jobController.getAllWaiting);
server.put('/jobs/assign/:id', [hasAnyRole("COMPANY")], jobController.assignCompanyToJob);
server.put('/jobs/unassign/:id', [hasAnyRole("COMPANY")], jobController.unassignCompanyFromJob);
server.get('/jobs/:id', [hasAnyRole("COMPANY", "CUSTOMER")], jobController.getById);
server.put('/jobs/:id', [hasAnyRole("CUSTOMER")], jobController.update);
server.delete('/jobs/:id', [hasAnyRole("CUSTOMER")], jobController.delete);
server.post('/jobs/search', [hasAnyRole("COMPANY")], jobController.search);

// Middleware: Error handling
server.use(apiErrorHandler);
