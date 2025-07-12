import {validateBody} from "../../../middleware/validation.middleware";

const multer = require('multer');
const path = require('path');
const fs = require('fs');
import { randomInt } from 'node:crypto';
import {UploadDto} from "./upload.dto";

export const storage = multer.diskStorage({
    destination: async function (req, file, cb) {
        const dto = await validateBody(req, UploadDto);

        const subfolder = path.join('uploads/', dto.jobId);

        if (!fs.existsSync(subfolder)) {
            fs.mkdirSync(subfolder, { recursive: true });
        }

        cb(null, subfolder);
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + randomInt(1, 1000) + path.extname(file.originalname));
    }
});

export const upload = multer({ storage });