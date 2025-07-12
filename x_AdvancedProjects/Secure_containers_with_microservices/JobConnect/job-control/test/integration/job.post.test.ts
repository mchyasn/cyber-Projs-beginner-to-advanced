import {beforeEach, describe, expect, it} from "vitest";
import {Job} from "../../src/persistence/models/job.model";
import request, {authorizedRequest, login} from "../request";



describe('POST /jobs/search', () => {
    beforeEach(async () => {
        await new Job({
            state: "waiting",
            title: "Looking for server cleaning",
            customerEmail: "customertest@jobsapp.com",
            description: "Clean my server",
            categories: ["Cleaning", "IT Services"],
            subcategories: ["Server cleaning"],
            budget: 500,

        }).save()
    });

    it('returns 200 for valid search', async () => {
        await login("company")
        const res = await authorizedRequest.post(`/jobs/search`)
            .send({
                text: "Looking",
                fields: ["title","description"]
            })
        console.log(res.body)
        expect(res.status).toBe(200);
    });

    it('returns 404 for invalid search', async () => {
        await login("company")
        const res = await authorizedRequest.post(`/jobs/search`)
            .send({
                text: "aaaaaaa",
                fields: ["title","description"]
            })
        console.log(res.body)
        expect(res.status).toBe(404);
    });

    it('returns 400 for bad input', async () => {
        await login("company")
        const res = await authorizedRequest.post(`/jobs/search`)
            .send({
                fields: ["title"]
            })
        console.log(res.body)
        expect(res.status).toBe(400);
    });

    it('returns 400 for bad input', async () => {
        await login("company")
        const res = await authorizedRequest.post(`/jobs/search`)
            .send({
                text: "Looking",
            })
        console.log(res.body)
        expect(res.status).toBe(400);
    });

    it('returns 403 forbidden', async () => {
        await login("customer")
        const res = await authorizedRequest.post(`/jobs/search`)
            .send({
                text: "Looking",
                fields: ["title","description"]
            })
        console.log(res.body)
        expect(res.status).toBe(403);
    });

    it('returns 401 unauthorized', async () => {
        const res = await request.post(`/jobs/search`)
            .send({
                text: "Looking",
                fields: ["title","description"]
            })
        console.log(res.body)
        expect(res.status).toBe(401);
    });
});

describe('POST /jobs', () => {
    beforeEach(async () => {
        await Job.deleteMany({});
    });

    it('returns 201 and creates a job with valid data', async () => {
        await login("customer");
        const jobData = {
            state: "waiting",
            title: "Full Stack Developer Needed",
            customerEmail: "customer@jobsapp.com",
            description: "Looking for experienced developer Looking for experienced developer",
            categories: ["IT Services"],
            subcategories: ["Web Development"],
            budget: 5000
        };
        const res = await authorizedRequest.post('/jobs').send(jobData);
        console.log(res.body)

        expect(res.status).toBe(201);
        expect(res.body).toMatchObject(jobData);

        const dbJob = await Job.findById(res.body._id);
        expect(dbJob).toBeTruthy();
        expect(dbJob?.title).toBe(jobData.title);
    });

    it('returns 400 for missing required title field', async () => {
        await login("customer");
        const res = await authorizedRequest.post('/jobs').send({
            customerEmail: "customer@test.com",
            description: "Job without title",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: 200
        });
        expect(res.status).toBe(400);
    });

    it('returns 400 for invalid budget type (string)', async () => {
        await login("customer");
        const res = await authorizedRequest.post('/jobs').send({
            state: "waiting",
            title: "Invalid Budget Job",
            customerEmail: "customer@test.com",
            description: "Test description",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: "not-a-number"
        });
        expect(res.status).toBe(400);
    });

    it('returns 400 for negative budget value', async () => {
        await login("customer");
        const res = await authorizedRequest.post('/jobs').send({
            state: "waiting",
            title: "Negative Budget Job",
            customerEmail: "customer@test.com",
            description: "Test description",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: -100
        });
        expect(res.status).toBe(400);
    });

    it('returns 400 for non-array categories', async () => {
        await login("customer");
        const res = await authorizedRequest.post('/jobs').send({
            state: "waiting",
            title: "Invalid Categories Job",
            customerEmail: "customer@test.com",
            description: "Test description",
            categories: "IT Services",
            subcategories: ["Support"],
            budget: 300
        });
        expect(res.status).toBe(400);
    });

    it('returns 403 forbidden for COMPANY role', async () => {
        await login("company");
        const res = await authorizedRequest.post('/jobs').send({
            state: "waiting",
            title: "Company-Created Job",
            customerEmail: "company@test.com",
            description: "Should not be allowed",
            categories: ["IT"],
            subcategories: ["Networking"],
            budget: 1000
        });
        expect(res.status).toBe(403);
    });

    it('returns 401 unauthorized for unauthenticated requests', async () => {
        const res = await request.post('/jobs').send({
            state: "waiting",
            title: "Unauthenticated Job",
            customerEmail: "anonymous@test.com",
            description: "Should not be created",
            categories: ["IT"],
            subcategories: ["Security"],
            budget: 500
        });
        expect(res.status).toBe(401);
    });
});