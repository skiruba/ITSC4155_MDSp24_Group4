package io.getarrays.server.models;

import io.getarrays.server.enumeration.Status;
import jakarta.persistence.*;
import jakarta.validation.constraints.NotEmpty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

//Server Model for saving Server Information to MySQL Database
//This is the model for each individual Server object.
// This can also models as a Table, a Server Table
@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Server {
    //primary key, auto-gen. if not provided.
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    //unique column, cannot be empty.
    @Column(unique = true)
    @NotEmpty(message = "IP Address cannot be empty or null")
    private String ipAddress;

    private String name;
    private String memory;
    private String type;
    private String imageUrl;
    private Status status;
}
