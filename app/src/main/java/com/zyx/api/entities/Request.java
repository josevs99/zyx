package com.zyx.api.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import java.time.LocalDateTime;
import java.util.UUID;
@Entity
@Table(name="requests")
public class Request {

    @Id
    private UUID id = UUID.randomUUID();

    private String operationName;
    private String status;

    @Column(columnDefinition = "jsonb")
    private String details;

    private LocalDateTime createdAt = LocalDateTime.now();

    public void setOperationName(String spawnService) {
        this.operationName = spawnService;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public void setDetails(String s) {
        this.details = s;
    }
}

