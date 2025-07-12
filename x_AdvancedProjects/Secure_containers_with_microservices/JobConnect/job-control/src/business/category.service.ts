import {JobDto} from "../api/controllers/job/job.dto";
import {Job} from "../persistence/models/job.model";
import {Category} from "../persistence/models/category.model";
import {Subcategory} from "../persistence/models/subcategory.model";
import {CategoryDto} from "../api/controllers/category/category.dto";

export const categoryService = {

    async getAllCategories() {
        return Category.find();
    },
    async getSubcategories(data: CategoryDto) {
        return Subcategory.find({
            categories: { $all: data.categories },
            $expr: { $eq: [ { $size: "$categories" }, data.categories.length ] }
        });
    }


}