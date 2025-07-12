import 'reflect-metadata';
import {Request, Response} from 'express';
import {validateBody} from "../../../middleware/validation.middleware";
import {jobsService} from "../../../business/jobs.service";
import {categoryService} from "../../../business/category.service";
import {CategoryDto} from "./category.dto";

export class CategoryController {

    async getAll(req: Request, res: Response) {
        const categories = await categoryService.getAllCategories();
        res.status(200).send(categories)
    }

    async getSubcategories(req: Request, res: Response) {
        const dto = await validateBody(req, CategoryDto)
        const subcategories = await categoryService.getSubcategories(dto)
        res.status(200).send(subcategories)
    }

}
