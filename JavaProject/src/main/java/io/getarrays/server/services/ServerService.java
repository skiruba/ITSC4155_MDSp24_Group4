package io.getarrays.server.services;

import io.getarrays.server.models.Server;

import java.io.IOException;
import java.util.Collection;

// This is where we define all the functionalities/features we want the application
// to have
public interface ServerService {
    Server createServer(Server server); // Create a server in the database
    Server pingServer(String ipAddress) throws IOException; // Pings server by ipAddress
    Collection<Server> listServers(int limit); // Lists all the servers, returns the first 'limit' number of rows
    Server getServer(Long id); // Returns a specific server by id
    Server updateServer(Server server); // Updates server info in database
    Boolean deleteServer(Long id); // Deletes server from database
}
