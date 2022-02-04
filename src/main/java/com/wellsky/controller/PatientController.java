package com.wellsky.controller;

import com.wellsky.model.Patient;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.HttpStatus;
import io.micronaut.http.MutableHttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;

import java.util.List;

import static io.micronaut.http.MediaType.APPLICATION_JSON;

@Controller("/api/v1/patients")
public class PatientController {

    @Operation(summary = "Retrieves a list of patients who have the specified favorite food for a meal delivery",
            description = "Fetch a list of patients who have opted into the food delivery service and have the specified favorite food.")
    @ApiResponse(responseCode = "200", description = "Patient list successfully retrieved",
            content = {
                    @Content(
                            mediaType = "application/json",
                            array = @ArraySchema(schema = @Schema(implementation = Patient.class))
                    )
            })
    @ApiResponse(responseCode = "400", description = "Invalid food category specified")

    @Get(uri="/food/{foodCategory}", produces = APPLICATION_JSON)
    public MutableHttpResponse<List<Patient>> getByFavoriteFood(String foodCategory) {
        return HttpResponse.status(HttpStatus.OK).body(List.of(new Patient("Granny", "New York",
                "https://my.picture.com/1234.png", List.of(Patient.Restaurant.TacoBell),
                List.of(Patient.Food.Mexican))));
    }

    @Operation(summary = "Retrieves a list of patients who have the specified favorite restaurant for a meal delivery",
            description = "Fetch a list of patients who have opted into the food delivery service and have the specified favorite restaurant.")
    @ApiResponse(responseCode = "200", description = "Patient list successfully retrieved",
            content = {
                    @Content(
                            mediaType = "application/json",
                            array = @ArraySchema(schema = @Schema(implementation = Patient.class))
                    )
            })
    @ApiResponse(responseCode = "400", description = "Invalid food category specified")

    @Get(uri="/restaurant/{restaurantName}", produces = APPLICATION_JSON)
    public MutableHttpResponse<List<Patient>> getByFavoriteRestaurant(String restaurantName) {
        return HttpResponse.status(HttpStatus.OK).body(List.of(new Patient("Granny", "New York",
                "https://my.picture.com/1234.png", List.of(Patient.Restaurant.TacoBell),
                List.of(Patient.Food.Mexican))));
    }
}
