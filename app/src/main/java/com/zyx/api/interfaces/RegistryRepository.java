package com.zyx.api.interfaces;

import com.zyx.api.entities.Registry;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface RegistryRepository  extends JpaRepository<Registry, UUID> {
}
