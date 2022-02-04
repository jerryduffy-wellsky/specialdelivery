package com.wellsky.model;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.util.List;

@Data
@RequiredArgsConstructor
@Schema(name="Patient", description="Patient response")
public class Patient {

    public enum Food {
        Pizza,
        Burger,
        Italian,
        Mexican,
        Steak,
        Bbq,
    }

    public enum Restaurant {
        BurgerKing,
        PapaJohns,
        TacoBell,
        SonnysBbq,
        BuffaloWildWings,
    }

    @Schema(description = "Patient's first name")
    private final String firstName;
    @Schema(description = "Patient's city")
    private final String city;
    @Schema(description = "URL to the patient's picture")
    private final String pictureUrl;
    @Schema(description = "List of Patient's favorite restaurants")
    private final List<Restaurant> favoriteRestaurants;
    @Schema(description = "List of Patient's favorite foods")
    private final List<Food> favoriteFoods;
}
