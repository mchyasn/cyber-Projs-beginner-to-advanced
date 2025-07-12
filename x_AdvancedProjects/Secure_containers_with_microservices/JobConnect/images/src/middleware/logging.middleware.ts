import path = require("node:path");
import * as fs from "node:fs";

export const loggingService = function (req, res, next) {
    const user = res.locals.oauth?.token?.user;
    if (!user) {
        return next();
    }

    const userEmail = user.email;
    const logFilePath = path.join(__dirname, '..','..', 'logs', `${userEmail}.log`);
    const startTime = Date.now();

    try {
        fs.mkdirSync(path.dirname(logFilePath), { recursive: true });
    } catch (err) {
        console.error("Failed to create log directory:", err);
        return next(err);
    }

    const requestData = {
        method: req.method,
        url: req.originalUrl,
        headers: req.headers,
        body: req.body,
        timestamp: new Date().toISOString(),
    };

    try {
        fs.appendFileSync(logFilePath, `\n[REQUEST]\n${JSON.stringify(requestData, null, 2)}\n`);
    } catch (err) {
        console.error("Failed to log request data:", err);
        return next(err);
    }

    const originalSend = res.send;
    let responseLogged = false;

    res.send = function (body) {
        if (!responseLogged) {
            responseLogged = true;
            const responseTime = Date.now() - startTime;

            const responseData = {
                status: res.statusCode,
                headers: res.getHeaders(),
                body,
                responseTime: `${responseTime}ms`,
                timestamp: new Date().toISOString(),
            };

            try {
                fs.appendFileSync(logFilePath, `\n[RESPONSE]\n${JSON.stringify(responseData, null, 2)}\n`);
            } catch (err) {
                console.error("Failed to log response data:", err);
            }
        }
        return originalSend.call(this, body);
    };

    next();
};
