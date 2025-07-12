export interface Job {
    _id: string | undefined;
    state: string | undefined;
    customerEmail: string | undefined,
    companyEmail: string | undefined
    title: string,
    description: string,
    categories: string[],
    subcategories: string[]| undefined,
    images: File[] | undefined,
    budget: number | undefined
}