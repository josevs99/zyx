package com.zyx.api.controller;

import com.zyx.api.entities.Registry;
import com.zyx.api.entities.ServiceEntity;
import com.zyx.api.interfaces.RegistryRepository;
import com.zyx.api.interfaces.ServiceRepository;
import com.zyx.api.service.ServiceManager;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/service")
public class ServiceController implements BaseController {

    private static final Logger log = LoggerFactory.getLogger(ServiceController.class);


    //private final ServiceManager serviceManager;

    /*public ServiceController(ServiceManager sm) {
        this.serviceManager = sm;
    }*/

    /*@PostMapping("/add")
    public ServiceEntity addService(@RequestBody ServiceEntity service) {
        return serviceManager.spawnService(service);
    }*/
    @Autowired
    private ServiceRepository serviceRepo;

    @PostMapping("/add")
    public String addService(@RequestParam("servicename") String serviceName ) throws Exception {

        log.info("Creating new service test" );
        try{
            ServiceEntity service = new ServiceEntity();
            service.setServiceName(serviceName);
            serviceRepo.save(service);

            log.info("saved succesfully service " + serviceName);
            return "Added " + serviceName;
        }catch(Exception e){
            log.error("Error during service add" + e.toString());
            throw new Exception("Error on add request");
        }

    }

    @GetMapping("/get/{id}")
    public String getService(@PathVariable("id") String id) throws Exception {
        Optional<ServiceEntity> sEntity = Optional.of(new ServiceEntity());
        UUID uuid = UUID.fromString(id);
        sEntity = serviceRepo.findById(uuid);
        ServiceEntity  se = new ServiceEntity();
        if(sEntity.isPresent()){
            se = sEntity.get();
            log.info("getting service name" + se.getServiceName());
            return se.getServiceName();
        }else{
            log.error("Instance not found " + id );
            throw new Exception("Instance not found "  + id );
        }

    }

    @PutMapping("/update/{id}")
    public String updateService(@PathVariable("id") String id, @RequestParam("servicename") String servicename) throws Exception {
        Optional<ServiceEntity> sEntity = Optional.of(new ServiceEntity());
        String result = "Succesfully updated " + id + " with new name " + servicename;
        UUID uuid = UUID.fromString(id);
        sEntity = serviceRepo.findById(uuid);
        ServiceEntity  se = new ServiceEntity();
        if(sEntity.isPresent()){
            se = sEntity.get();
            se.setServiceName(servicename);
            serviceRepo.save(se);
        }else{
            log.error("Instance not found "+ id);
            throw new Exception("Instance not found " + id);
        }
        return result;
    }

}
