import {JobDto} from "../api/controllers/job/job.dto";
import {Job} from "../persistence/models/job.model";
import {SearchDto} from "../api/controllers/job/search.dto";

export const jobsService = {
    async create(data: JobDto) {
        const job = new Job(data)
        await job.save()
        return job
    },

    async getAll() {
        return Job.find();
    },

    async getWaiting() {
        return Job.find({"state" : "waiting"});
    },

    async getById(id: string) {
        return Job.findById(id);
    },

    async update(id: string, data: JobDto) {
        return Job.findByIdAndUpdate(id, data, {new: true});
    },

    async delete(id: string, email: string) {
        const job = await Job.findById(id)
        if(job.customerEmail == email){
            return Job.findByIdAndDelete(id);
        }
        else{
            console.error(`Email: ${email} does not match the job owner's ${job.customerEmail} email.`);
        }
    },

    async assignCompany(jobId: string, email: string) {
        const job = await Job.findById(jobId);
        if(job.companyEmail == undefined || job.companyEmail == "" || job.companyEmail == email) {
            job.companyEmail = email;
            job.state = "assigned"
            await job.save();
            return job;
        } else {
            console.error(`Company email is already assigned to ${job.companyEmail}`);
        }
    },

    async unassignCompany(jobId: string, email: string) {
        const job = await Job.findById(jobId);
        if(job.companyEmail == email){
            job.companyEmail = undefined;
            job.state = "waiting"
            await job.save();
            return job;
        }
        else {
            console.error(`The provided email: ${email} does not match the company's assigned email: ${job.companyEmail}`);
        }
    },

    async getJobByCustomer(customerEmail: string) {
        return Job.find({"customerEmail" : customerEmail})
    },

    async getJobByCompany(companyEmail: string) {
        return Job.find({"companyEmail" : companyEmail})
    },

    async search(data: SearchDto) {
        try {
            if (!data.fields || data.fields.length === 0) {
                console.error("No fields provided for search.");
            }

            const searchConditions = {
                $and: [
                    { "state": "waiting" },
                    {
                        $or: data.fields.map(field => ({
                            [field]: { $regex: data.text, $options: 'i' }
                        }))
                    }
                ]
            };

            const jobs = await Job.find(searchConditions);

            return jobs;
        } catch (error) {
            console.error("Error during search:", error);
            throw error;
        }
    }


}