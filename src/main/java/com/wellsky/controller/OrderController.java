package com.wellsky.controller;

import com.wellsky.model.Order;
import com.wellsky.model.Patient;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.HttpStatus;
import io.micronaut.http.MutableHttpResponse;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;

import java.util.List;

import static io.micronaut.http.MediaType.APPLICATION_JSON;

@Controller("/api/v1/patients/{patientId}/orders")
public class OrderController {

    @Operation(summary = "Retrieves a list of orders for the target patient",
            description = "Fetch a list of orders made on behalf of the target patient")
    @ApiResponse(responseCode = "200", description = "Order list successfully retrieved",
            content = {
                    @Content(
                            mediaType = "application/json",
                            array = @ArraySchema(schema = @Schema(implementation = Order.class))
                    )
            })
    @ApiResponse(responseCode = "404", description = "Target patient not found")

    @Get(produces = APPLICATION_JSON)
    public MutableHttpResponse<List<Order>> getOrderForPatient(long patientId) {
        return HttpResponse.status(HttpStatus.OK).body(List.of(new Order()));
    }

    @Operation(summary = "Create a new Order for the target patient",
            description = "Create a new order made on behalf of the target patient")
    @ApiResponse(responseCode = "201", description = "Order list successfully created",
            content = {
                    @Content(
                            mediaType = "application/json",
                            array = @ArraySchema(schema = @Schema(implementation = Order.class))
                    )
            })
    @ApiResponse(responseCode = "404", description = "Target patient not found")

    @Post(produces = APPLICATION_JSON)
    public MutableHttpResponse<List<Order>> newOrderForPatient(long patientId, @Body Order order) {
        return HttpResponse.status(HttpStatus.OK).body(List.of(new Order()));
    }
}
