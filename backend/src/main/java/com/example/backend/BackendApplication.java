package com.example.backend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.jdbc.core.JdbcTemplate;

@SpringBootApplication
public class BackendApplication {

    public static void main(String[] args) {
        SpringApplication.run(BackendApplication.class, args);
    }
    
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Bean
    public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
        return args -> {
            try {
                jdbcTemplate.execute("SELECT 1"); // Execute a simple query
                System.out.println("Database connection test successful!");
            } catch (Exception e) {
                System.out.println("Failed to connect to the database: " + e.getMessage());
            }
        };
    }
}
