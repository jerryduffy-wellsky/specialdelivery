package com.wellsky.controller;

import com.wellsky.model.About;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.HttpStatus;
import io.micronaut.http.MediaType;
import io.micronaut.http.MutableHttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Produces;

import java.time.Instant;

@Controller("/about")
public class AboutController {
    @Get
    @Produces(MediaType.APPLICATION_JSON)
    public MutableHttpResponse<About> about() {
        return HttpResponse.status(HttpStatus.OK).body(
                new About(
                        "Special Delivery",
                        "Connecting Caring Individuals to Home Bound Patients Through Food Order & Delivery",
                        "1.0.0",
                        Instant.now()
                )
        );
    }
}
