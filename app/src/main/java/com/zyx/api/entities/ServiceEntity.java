package com.zyx.api.entities;

import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name="services")
public class ServiceEntity {

    @Id
    private UUID id = UUID.randomUUID();

    private String serviceName;

    @Enumerated(EnumType.STRING)
    private Status status;

    @Column(columnDefinition = "jsonb")
    private String details;

    private LocalDateTime startedAt;
    private LocalDateTime endedAt;

    public String getServiceName() {
        return this.serviceName;
    }

    public void setServiceName(String serviceName){
        this.serviceName = serviceName;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public void setStartedAt(LocalDateTime now) {
    }

    // Status Enum
    public enum Status {
        PENDING,
        RUNNING,
        FAILED,
        DONE
    }

}


