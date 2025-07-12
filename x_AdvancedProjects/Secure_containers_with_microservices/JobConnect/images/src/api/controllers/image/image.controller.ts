import 'reflect-metadata';
import {validateParams} from "../../../middleware/validation.middleware";
import {IdParam} from "../../../types/base.dto";
const path = require('path');
const fs = require('fs');


export class ImageController {

    async getImages(req, res) {

        const {id} = await validateParams(req, IdParam);
        const imageDir = path.join(__dirname, "..", "..","..","..", 'uploads', id);

        if (!fs.existsSync(imageDir)) {
            return res.status(404).json({message: `No images found for job: ${id}`});
        }

        const images: string = fs.readdirSync(imageDir).map(image => {
            return `${req.protocol}://${req.get('host')}/uploads/${id}/${image}`;
        });

        res.status(200).send(images);


    }

    async uploadImages(req, res, next) {
        try {
            const files = req.files as Express.Multer.File[];

            const fileUrls = files.map(file => {
                return `${req.protocol}://${req.get('host')}/uploads/${req.body.jobId}/${file.filename}`;
            });

            res.json({
                message: "Files uploaded successfully!",
                fileUrls: fileUrls
            });
        } catch (error) {
            next(error);
        }
    }




}
