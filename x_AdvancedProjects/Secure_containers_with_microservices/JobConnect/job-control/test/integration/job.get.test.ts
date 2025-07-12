import {beforeEach, describe, expect, it} from "vitest";
import {Job} from "../../src/persistence/models/job.model";
import request, {authorizedRequest, login} from "../request";
import {Types} from "mongoose";

describe('GET /jobs/company', () => {
    beforeEach(async () => {
        // Setup jobs for the company user and others
        const companyJob = new Job({
            _id: new Types.ObjectId('b00000000000000000000001'),
            state: "assigned",
            title: "Company Job",
            customerEmail: "customer@test.com",
            companyEmail: "company@jobsapp.com",
            description: "Company job description",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: 200
        });
        const otherJob = new Job({
            _id: new Types.ObjectId('b00000000000000000000002'),
            state: "assigned",
            title: "Other Company Job",
            customerEmail: "customer@test.com",
            companyEmail: "other@company.com",
            description: "Other company job",
            categories: ["Cleaning"],
            subcategories: ["Office"],
            budget: 300
        });
        await companyJob.save();
        await otherJob.save();
    });

    it('returns 200 with company jobs', async () => {
        await login("company");
        const res = await authorizedRequest.get('/jobs/company');
        expect(res.status).toBe(200);
        expect(res.body).toBeInstanceOf(Array);
        expect(res.body.length).toBe(1);
        expect(res.body[0].companyEmail).toBe('company@jobsapp.com');
    });

    it('returns 404 if no jobs found for company', async () => {
        await Job.deleteMany({});
        await login("company");
        const res = await authorizedRequest.get('/jobs/company');
        expect(res.status).toBe(404);
        expect(res.body.error).toBe('Not found');
    });

    it('returns 403 for customer role', async () => {
        await login("customer");
        const res = await authorizedRequest.get('/jobs/company');
        expect(res.status).toBe(403);
    });

    it('returns 401 if unauthorized', async () => {
        const res = await request.get('/jobs/company');
        expect(res.status).toBe(401);
    });
});

describe('GET /jobs/customer', () => {
    beforeEach(async () => {
        const customerJob = new Job({
            _id: new Types.ObjectId('c00000000000000000000001'),
            state: "waiting",
            title: "Customer Job",
            customerEmail: "customer@jobsapp.com",
            description: "Customer job description",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: 200
        });
        const otherJob = new Job({
            _id: new Types.ObjectId('c00000000000000000000002'),
            state: "waiting",
            title: "Other Customer Job",
            customerEmail: "other@customer.com",
            description: "Other customer job",
            categories: ["Cleaning"],
            subcategories: ["Office"],
            budget: 300
        });
        await customerJob.save();
        await otherJob.save();
    });

    it('returns 200 with customer jobs', async () => {
        await login("customer");
        const res = await authorizedRequest.get('/jobs/customer');
        expect(res.status).toBe(200);
        expect(res.body.length).toBe(1);
        expect(res.body[0].customerEmail).toBe('customer@jobsapp.com');
    });

    it('returns 404 if no jobs found for customer', async () => {
        await Job.deleteMany({});
        await login("customer");
        const res = await authorizedRequest.get('/jobs/customer');
        expect(res.status).toBe(404);
        expect(res.body.error).toBe('Not found');
    });

    it('returns 403 for company role', async () => {
        await login("company");
        const res = await authorizedRequest.get('/jobs/customer');
        expect(res.status).toBe(403);
    });

    it('returns 401 if unauthorized', async () => {
        const res = await request.get('/jobs/customer');
        expect(res.status).toBe(401);
    });
});


describe('GET /jobs (all waiting)', () => {
    beforeEach(async () => {
        const waitingJob = new Job({
            _id: new Types.ObjectId('d00000000000000000000001'),
            state: "waiting",
            title: "Waiting Job",
            customerEmail: "customer@test.com",
            description: "Waiting job description",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: 200
        });
        const assignedJob = new Job({
            _id: new Types.ObjectId('d00000000000000000000002'),
            state: "assigned",
            title: "Assigned Job",
            customerEmail: "customer@test.com",
            companyEmail: "company@jobsapp.com",
            description: "Assigned job description",
            categories: ["Cleaning"],
            subcategories: ["Office"],
            budget: 300
        });
        await waitingJob.save();
        await assignedJob.save();
    });

    it('returns 200 with waiting jobs', async () => {
        await login("company");
        const res = await authorizedRequest.get('/jobs');
        expect(res.status).toBe(200);
        const allWaiting = res.body.every(job => job.state === 'waiting');
        expect(allWaiting).toBe(true);
        expect(res.body.some(job => job._id === 'd00000000000000000000001')).toBe(true);
        expect(res.body.some(job => job._id === 'd00000000000000000000002')).toBe(false);
    });

    it('returns 200 with empty array if no waiting jobs', async () => {
        await Job.deleteMany({});
        await login("company");
        const res = await authorizedRequest.get('/jobs');
        expect(res.status).toBe(200);
        expect(res.body).toEqual([]);
    });

    it('returns 403 for customer role', async () => {
        await login("customer");
        const res = await authorizedRequest.get('/jobs');
        expect(res.status).toBe(403);
    });

    it('returns 401 if unauthorized', async () => {
        const res = await request.get('/jobs');
        expect(res.status).toBe(401);
    });
});

describe('GET /jobs/:id', () => {
    let existingJobId: string;
    beforeEach(async () => {
        const job = new Job({
            _id: new Types.ObjectId('e00000000000000000000001'),
            state: "waiting",
            title: "Test Job",
            customerEmail: "customer@test.com",
            description: "Test job description",
            categories: ["IT"],
            subcategories: ["Support"],
            budget: 200
        });
        await job.save();
        existingJobId = job._id.toString();
    });

    it('returns 200 for existing job', async () => {
        await login("company");
        const res = await authorizedRequest.get(`/jobs/${existingJobId}`);
        expect(res.status).toBe(200);
        expect(res.body._id).toBe(existingJobId);
    });

    it('returns 404 for non-existent job', async () => {
        await login("customer");
        const nonExistentId = new Types.ObjectId().toString();
        const res = await authorizedRequest.get(`/jobs/${nonExistentId}`);
        expect(res.status).toBe(404);
    });

    it('returns 400 for invalid job id', async () => {
        await login("company");
        const res = await authorizedRequest.get('/jobs/invalid-id');
        expect(res.status).toBe(400);
    });

    it('returns 401 if unauthorized', async () => {
        const res = await request.get(`/jobs/${existingJobId}`);
        expect(res.status).toBe(401);
    });

    it('allow both COMPANY and CUSTOMER roles', async () => {
        await login("company");
        const resCompany = await authorizedRequest.get(`/jobs/${existingJobId}`);
        expect(resCompany.status).toBe(200);

        await login("customer");
        const resCustomer = await authorizedRequest.get(`/jobs/${existingJobId}`);
        expect(resCustomer.status).toBe(200);
    });
});