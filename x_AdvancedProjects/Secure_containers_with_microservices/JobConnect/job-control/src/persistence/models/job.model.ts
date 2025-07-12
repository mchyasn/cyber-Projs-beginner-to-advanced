
import * as mongoose from "mongoose";

export const Job = mongoose.model('Job', new mongoose.Schema({
    state: { type: String, required: true },
    title: { type: String, required: true },
    customerEmail:{ type: String, required: true },
    companyEmail: { type: String, required: false },
    description: { type: String, required: true },
    categories: { type: [String], required: true },
    subcategories: { type: [String], required: false, default: undefined }, //undefined so it doesnt appear in mongo.
    images: { type: [Object], required: false, default: undefined },
    budget: { type: Number, required: false },
}));
