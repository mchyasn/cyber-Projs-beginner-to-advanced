import mongoose from "mongoose";

export const Subcategory = mongoose.model('Subcategory', new mongoose.Schema({
    _id: { type: String, required: true },
    name: { type: String, required: true },
    categories: { type: [String], required: true },
},{collection: "subcategory"}));