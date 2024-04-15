package com.jordandesotle.autominecraft.utils;

import java.io.File;

public class LiveExportManager {

    private static String savePath = "/home/jordan/Documents/AutoMinecraft_Root/neural_network/data/input";

    public LiveExportManager() {
        createDirectories();
    }

    private boolean createDirectories() {

        File gameOutputDir = new File(savePath);
        if(!createDirectoryIfNotExist(gameOutputDir)) {
            return false;
        }
        return true;
    }

    // When provided a path, this function will check if it exists before creating it
    public boolean createDirectoryIfNotExist(File path) {

        // Check to see if the path exists first
        if(!path.exists()) {
            try {
                // Attempt to create the directory
                if (path.mkdirs()) {
                    System.out.println("Directory (" + path.getPath() + ") created successfully.");
                    return true;
                }
                System.err.println("Failed to create directory.");
                return false;

            } catch (SecurityException e) {
                System.err.println("SecurityException: " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.err.println("IllegalArgumentException: " + e.getMessage());
            }
            return false;
        }
        return true;
    }

    public File getSavePath() {
        return new File(savePath);
    }

}
