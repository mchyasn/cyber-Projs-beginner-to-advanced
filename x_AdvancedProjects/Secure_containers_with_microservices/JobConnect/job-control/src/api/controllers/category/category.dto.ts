import {
    IsNotEmpty,
    Length,
    IsArray,
    IsOptional,
    IsNumber,
    IsPositive,
    ArrayMinSize,
    IsEmail
} from 'class-validator';

export class CategoryDto {

    @IsArray()
    @IsNotEmpty({ each: true })
    @ArrayMinSize(1)
    categories: string[];

}


