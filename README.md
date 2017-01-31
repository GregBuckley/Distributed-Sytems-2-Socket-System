# Lab2FIXED

# Distributed Systems - Lab 2
Student Name: Gregory Buckley
Student ID: 13325220

This assignment has been written using Python 2.7.

The code represents a simple socket system with the follwowing behaviour:
Open a server socket connection
    Wait for clients to connect
    When a client connects, handle the client requests
    Go back to waiting for a client connection.

The client is hosted on a debian node at 10.62.0.158, which connects to port 8000 on another debian node located at 10.62.0.148. 

Code to run: "python client.py -start 8079" (to run on port 8079 for example)

