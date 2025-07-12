import {beforeEach, describe, expect, it} from "vitest";
import {Job} from "../../src/persistence/models/job.model";
import request, {authorizedRequest, login} from "../request";
import {Types} from "mongoose";
describe('PUT /jobs/assign', () => {

    beforeEach(async () => {
       const jobUnassigned = new Job({
           _id: new Types.ObjectId('a00000000000000000000001'),
           state: "waiting",
           title: "Looking for server cleaning",
           customerEmail: "customertest@jobsapp.com",
           description: "Clean my server",
           categories: ["Cleaning", "IT Services"],
           subcategories: ["Server cleaning"],
           budget: 100
       })
        const jobAssigned = new Job({
            _id: new Types.ObjectId('a00000000000000000000002'),
            state: "assigned",
            title: "Looking for server cleaning",
            customerEmail: "customertest@jobsapp.com",
            companyEmail: "company@jobsapp.com",
            description: "Clean my server",
            categories: ["Cleaning", "IT Services"],
            subcategories: ["Server cleaning"],
            budget: 100
        })
        await jobUnassigned.save();
       await jobAssigned.save();
    });

    it('returns 200 for valid assign', async () => {
        await login("company")
        const res = await authorizedRequest.put(`/jobs/assign/a00000000000000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(200);
        expect(res.body.state).toBe("assigned")
        expect(res.body.companyEmail).toBe('company@jobsapp.com');
    });

    it('returns 400 for invalid assign', async () => {
        await login("company")
        const res = await authorizedRequest.put(`/jobs/assign/a00000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(400);
    });

    it('returns 403 forbidden', async () => {
        await login("customer")
        const res = await authorizedRequest.put(`/jobs/assign/a00000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(403);
    });

    it('returns 401 unauthorized', async () => {
        const res = await request.put(`/jobs/assign/a00000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(401);
    });

});


describe('PUT /jobs/unassign', () => {

    beforeEach(async () => {
        const jobUnassigned = new Job({
            _id: new Types.ObjectId('a00000000000000000000001'),
            state: "waiting",
            title: "Looking for server cleaning",
            customerEmail: "customertest@jobsapp.com",
            description: "Clean my server",
            categories: ["Cleaning", "IT Services"],
            subcategories: ["Server cleaning"],
            budget: 100
        })
        const jobAssigned = new Job({
            _id: new Types.ObjectId('a00000000000000000000002'),
            state: "assigned",
            title: "Looking for server cleaning",
            customerEmail: "customertest@jobsapp.com",
            companyEmail: "company@jobsapp.com",
            description: "Clean my server",
            categories: ["Cleaning", "IT Services"],
            subcategories: ["Server cleaning"],
            budget: 100
        })
        await jobUnassigned.save();
        await jobAssigned.save();
    });

    it('returns 200 for valid unassign', async () => {
        await login("company")
        const res = await authorizedRequest.put(`/jobs/unassign/a00000000000000000000002`)
            .send()
        console.log(res.body);
        expect(res.status).toBe(200);
        expect(res.body.state).toBe("waiting")
        expect(res.body.companyEmail).toBe(undefined);
    });

    it('returns 400 for invalid unassign', async () => {
        await login("company")
        const res = await authorizedRequest.put(`/jobs/unassign/a00000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(400);
    });

    it('returns 403 forbidden', async () => {
        await login("customer")
        const res = await authorizedRequest.put(`/jobs/unassign/a00000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(403);
    });

    it('returns 401 unauthorized', async () => {
        const res = await request.put(`/jobs/unassign/a00000000000001`)
            .send()
        console.log(res.body)
        expect(res.status).toBe(401);
    });

});
