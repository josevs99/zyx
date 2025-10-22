package com.zyx.api.entities;

import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name="registries")
public class Registry {

    @Id
    private UUID id = UUID.randomUUID();

    private String operation;

    private int status;

    private LocalDateTime createdAt = LocalDateTime.now();
    private LocalDateTime updatedAt = LocalDateTime.now();

    public void setOperation(String s) {
    }

    public void setStatus(ServiceEntity.Status status) {
    }
}
