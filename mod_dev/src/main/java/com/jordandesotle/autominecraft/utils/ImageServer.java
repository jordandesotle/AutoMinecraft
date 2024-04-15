package com.jordandesotle.autominecraft.utils;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.io.OutputStream;

public class ImageServer {

    private ServerSocket serverSocket;
    private Socket clientSocket = null;
    private boolean isRunning;

    public ImageServer(int port) {
        try {
            serverSocket = new ServerSocket(port);
            isRunning = true;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void startServer() {
        new Thread(() -> {
            while (isRunning) {
                try {
                    Socket client = serverSocket.accept();
                    clientSocket = client;
                    System.out.println("Connected to client: " + clientSocket.getInetAddress());

                    // Send a message to the client
                    sendMessage(client, "You are connected");

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
        System.out.println("Server started and listening for connections...");
    }

    public void stopServer() {
        try {
            serverSocket.close();
            isRunning = false;
            System.out.println("Server stopped.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Socket getClientSocket() {
        return clientSocket;
    }

    public void sendMessage(Socket clientSocket, String message) {

        if (clientSocket == null) {
            System.out.println("No client connection available. Cannot send message.");
            return;
        }

        try {
            OutputStream outputStream = clientSocket.getOutputStream();
            outputStream.write(message.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}