package com.wellsky.model;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

import java.time.Instant;

@Getter
@Setter
@RequiredArgsConstructor
public class About {
    private final String projectName;
    private final String description;
    private final String version;
    private final Instant buildTimestamp;
}
