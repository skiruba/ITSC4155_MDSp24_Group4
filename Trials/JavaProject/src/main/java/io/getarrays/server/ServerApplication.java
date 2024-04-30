package io.getarrays.server;

import io.getarrays.server.enumeration.Status;
import io.getarrays.server.models.Server;
import io.getarrays.server.repo.ServerRepo;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import static io.getarrays.server.enumeration.Status.*;

@SpringBootApplication
public class ServerApplication {

	public static void main(String[] args) {
		//
		SpringApplication.run(ServerApplication.class, args);
	}

	@Bean
	CommandLineRunner run(ServerRepo serverRepo){
		return args -> {
			serverRepo.save(new Server(null, "192.168.1.227", "Windows", "16 GB", "Personal PC",
					"http://localhost:8080/server/image/server1.png", SERVER_UP));
			serverRepo.save(new Server(null, "192.168.1.68", "MockServer1", "16 GB", "Mock",
					"http://localhost:8080/server/image/server1.png", SERVER_UP));
			serverRepo.save(new Server(null, "192.168.1.35", "MockServer2", "32 GB", "Mock",
					"http://localhost:8080/server/image/server1.png", SERVER_UP));
			serverRepo.save(new Server(null, "192.168.1.14", "MockServer3", "64 GB", "Mock",
					"http://localhost:8080/server/image/server1.png", SERVER_UP));
		};

	}

}
