package io.getarrays.server.services.implementation;

import io.getarrays.server.enumeration.Status;
import io.getarrays.server.models.Server;
import io.getarrays.server.repo.ServerRepo;
import io.getarrays.server.services.ServerService;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.io.IOException;
import java.net.InetAddress;
import java.util.Collection;
import java.util.Random;

@RequiredArgsConstructor
@Service
@Transactional
@Slf4j
public class ServerServiceImpl implements ServerService {
    private final ServerRepo serverRepo;

    /**
     * @param server
     * @return
     */
    @Override
    public Server createServer(Server server) {
        log.info("Saving new server: {}", server.getName());
        server.setImageUrl(setServerImageUrl());
        return serverRepo.save(server);
    }



    /**
     * @param ipAddress
     * @return
     */
    @Override
    public Server pingServer(String ipAddress) throws IOException {
        log.info("Pinging server IP: {}", ipAddress);
        Server server = serverRepo.findByIpAddress(ipAddress);
        InetAddress address = InetAddress.getByName(ipAddress);
        server.setStatus(address.isReachable(10000) ? Status.SERVER_UP : Status.SERVER_DOWN);
        serverRepo.save(server);
        return server;
    }

    /**
     * @param limit
     * @return
     */
    @Override
    public Collection<Server> listServers(int limit) {
        log.info("Fetching all servers");
        return serverRepo.findAll(PageRequest.of(0, limit)).toList();
    }

    /**
     * @param id
     * @return
     */
    @Override
    public Server getServer(Long id) {
        log.info("Fetching server by id {}", id);
        return serverRepo.findById(id).get();
    }

    /**
     * @param server
     * @return
     */
    @Override
    public Server updateServer(Server server) {
        log.info("Updating server: {}", server.getName());
        return serverRepo.save(server);
    }

    /**
     * @param id
     * @return
     */
    @Override
    public Boolean deleteServer(Long id) {
        log.info("Deleting server by ID: {}", id);
        serverRepo.deleteById(id);
        return Boolean.TRUE;
    }

    private String setServerImageUrl() {
        String[] imageNames = { "server1.png", "server2.png", "server3.png", "server4.png"};
        int randomIntGen = new Random().nextInt(4);
        return ServletUriComponentsBuilder.fromCurrentContextPath().path("/server/image/" + imageNames[randomIntGen]).toUriString();
    }
}
