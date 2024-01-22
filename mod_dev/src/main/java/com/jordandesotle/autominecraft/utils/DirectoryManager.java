package com.jordandesotle.autominecraft.utils;

import java.awt.image.BufferedImage;
import java.io.File;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DirectoryManager {

    private final String gameOutputPath = "/home/jordan/Documents/AutoMinecraft_Root/neural_network/data/game_output/";         // folder that contains all output from game
    private final String actionName = "mine_tree";                                                                              // folder that defines overall action to be learned
    private final String[] subfolderNames = {"align_with_tree", "move_to_tree", "break_tree", "success"};                       // different sub-actions we want to capture

    public DirectoryManager() {

        // Creates the outline for the images to be exported to
        if(!createDirectories()) {
            System.out.println("Failed to create one or more directories");
        }
        System.out.println("Successfully created all folders");
    }

    // Creates the outline directories
    private boolean createDirectories() {

        File gameOutputDir = new File(gameOutputPath);
        if(!createDirectoryIfNotExist(gameOutputDir)) {
            return false;
        }

        // Check to see if exists
        File actionDir = new File(gameOutputPath, actionName);
        if(!createDirectoryIfNotExist(actionDir)) {
            return false;
        }

        // Create all subfolders
        for(String subfolder : subfolderNames) {
            File subfolderDir = new File(actionDir, subfolder);
            if(!createDirectoryIfNotExist(subfolderDir)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Creates the specified directory if it does not exist
    */
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


    // Checks the given folder for the highest "setX" where X is a number and returns the next highest number
    public int getSetIndex(String directoryPath) {

        File directory = new File(directoryPath);
        if (!directory.exists()) {
            throw new IllegalArgumentException("Directory does not exist: " + directoryPath);
        }

        String[] files = directory.list();

        Pattern pattern = Pattern.compile("^set(\\d+)$");
        int maxNumber = 0;

        if (files != null) {
            for (String fileName : files) {
                Matcher matcher = pattern.matcher(fileName);

                if (matcher.matches()) {
                    int number = Integer.parseInt(matcher.group(1));
                    maxNumber = Math.max(maxNumber, number);
                }
            }
        }
        return maxNumber + 1;
    }

    public File getSavePath(int index) {

        File actionPath = getActionPath();

        return new File(actionPath, getSubfolderNameByIndex(index));
    }


    private File getActionPath() {
        return new File(gameOutputPath, actionName);
    }

    public String getOutputPath() {
        return gameOutputPath;
    }

    public int getNumSubActions() {
        return subfolderNames.length;
    }

    public String getSubfolderNameByIndex(int index) {
        if(index < 0 || index >= subfolderNames.length) {
            System.err.println("Index out of range");
        }
        return subfolderNames[index];
    }

}
