package com.zyx.api.service;

import com.zyx.api.entities.Registry;
import com.zyx.api.entities.Request;
import com.zyx.api.entities.ServiceEntity;
import com.zyx.api.interfaces.RegistryRepository;
import com.zyx.api.interfaces.RequestRepository;
import com.zyx.api.interfaces.ServiceRepository;
import jakarta.transaction.Transactional;

import java.time.LocalDateTime;

public class ServiceManager {

    private final RegistryRepository registryRepo;
    private final RequestRepository requestRepo;
    private final ServiceRepository serviceRepo;

    public ServiceManager(RegistryRepository r, RequestRepository req, ServiceRepository s) {
        this.registryRepo = r;
        this.requestRepo = req;
        this.serviceRepo = s;
    }

    @Transactional
    public ServiceEntity spawnService(ServiceEntity service) {
        // 1. Create registry record
        Registry registry = new Registry();
        registry.setOperation("Spawn Service: " + service.getServiceName());
        registry.setStatus(ServiceEntity.Status.PENDING);
        registryRepo.save(registry);

        // 2. Create request record
        Request request = new Request();
        request.setOperationName("Spawn Service");
        request.setStatus("PENDING");
        request.setDetails("{\"serviceName\":\"" + service.getServiceName() + "\"}");
        requestRepo.save(request);

        // 3. Spawn dummy service (simulate)
        service.setStatus(ServiceEntity.Status.RUNNING);
        service.setStartedAt(LocalDateTime.now());
        serviceRepo.save(service);

        // 4. Update registry/request
        registry.setStatus(ServiceEntity.Status.DONE);
        registryRepo.save(registry);

        request.setStatus("DONE");
        requestRepo.save(request);

        return service;
    }
}
