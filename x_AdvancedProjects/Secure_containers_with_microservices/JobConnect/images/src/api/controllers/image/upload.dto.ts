import {IsNotEmpty} from "class-validator";

export class UploadDto {
    @IsNotEmpty()
    jobId: string;
}
