package com.wellsky;

import io.micronaut.runtime.Micronaut;
import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Info;

@OpenAPIDefinition(
        info = @Info(
                title = "special-delivery-service",
                version = "1.0",
                description = "Special Delivery microservice"))
public class Application {

    public static void main(String[] args) {
        Micronaut.run(Application.class, args);
    }
}
