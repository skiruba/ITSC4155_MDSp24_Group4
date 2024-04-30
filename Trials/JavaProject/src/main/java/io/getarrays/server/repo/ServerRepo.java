package io.getarrays.server.repo;

import io.getarrays.server.models.Server;
import org.springframework.data.jpa.repository.JpaRepository;

// Extending JpaRepository is how we interact with, and manage information/data
// in the database
public interface ServerRepo extends JpaRepository<Server, Long> {

    Server findByIpAddress(String ipAddress);

}
