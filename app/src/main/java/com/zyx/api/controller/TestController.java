package com.zyx.api.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

@RestController
@RequestMapping("/api/test")
public class TestController {

    @GetMapping("/hello")
    public String hello() throws SQLException {

        String url = "jdbc:postgresql://localhost:26257/my_database?sslmode=disable";
        Connection conn = DriverManager.getConnection(url, "root", "");
        System.out.println("Connected!");

        return "Hello from TestController!";

    }
}

