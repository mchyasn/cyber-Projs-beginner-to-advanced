import mongoose from "mongoose";

export const Category = mongoose.model('Category', new mongoose.Schema({
    _id: { type: String, required: true },
    name: { type: String, required: true },
},{collection: "category"}));