package com.jordandesotle.autominecraft.utils;

import net.minecraft.client.Minecraft;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.client.event.InputEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

import org.lwjgl.BufferUtils;
import org.lwjgl.glfw.GLFW;
import org.lwjgl.opengl.GL11;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.lwjgl.opengl.GL11.*;

public class CaptureScreen {

    // Specify the absolute directory path
    String absolutePath = "/home/jordan/Documents/AutoMinecraft_Root/neural_network/data/game_output/";
    String folderName = "mine_tree";

    // Determines if screenshots will be taken
    private boolean takeScreenshots = false;
    private int index = 0;
    private int setIndex = 0;

    private int frameCount = 0;
    private int screenshotCounter = 1;

    // Image constants and Minecraft instance info
    private static final int BPP = 4; // bytes per pixel (RGBA)
    private static final int TYPE = GL_UNSIGNED_BYTE;
    private static final int FORMAT = GL_RGBA;
    private static final Minecraft MC = Minecraft.getInstance();
    private final Dimension dim;

    public CaptureScreen() {
        dim = getCurrentDimension();
    }

    private Dimension getCurrentDimension() {
        return new Dimension(MC.getWindow().getWidth(), MC.getWindow().getHeight());
    }

    @SubscribeEvent
    public void onRenderTick(TickEvent.RenderTickEvent event) {
        if (event.phase == TickEvent.Phase.END) {

            // Only take pictures while in the game and taking screenshots is enabled
            if (MC.player != null && !MC.isPaused() && takeScreenshots) {

                // Increment frame count on each render tick
                frameCount++;

                // Capture screenshot every 30 frames
                if (frameCount % 30 == 0) {
                    captureScreenshot();
                }
            }
        }
    }

    @SubscribeEvent
    public void onKeyInput(InputEvent.Key event) {
        if (event.getAction() == GLFW.GLFW_PRESS) {
            // Check if the pressed key is 'K'
            if (event.getKey() == GLFW.GLFW_KEY_K) {
                // Increment index when disabling screenshots
                if (takeScreenshots) {
                    index++;
                    screenshotCounter = 1;
                }
                // Invert the value of takeScreenshots
                takeScreenshots = !takeScreenshots;

                System.out.println("takeScreenshots is now: " + takeScreenshots);
            }
        }
    }

    public void captureScreenshot() {

        System.out.println("Screenshot triggered");

        // Create buffer
        int bufferSize = dim.height * dim.width * BPP; // 4 bytes per pixel (RGBA)
        ByteBuffer buffer = BufferUtils.createByteBuffer(bufferSize);

        glPixelStorei(GL_PACK_ALIGNMENT, 1);
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

        GL11.glReadPixels(0, 0, dim.width, dim.height, FORMAT, TYPE, buffer);

        BufferedImage image = new BufferedImage(dim.width, dim.height, BufferedImage.TYPE_INT_ARGB);
        for (int y = 0; y < dim.height; y++) {
            for (int x = 0; x < dim.width; x++) {
                int bufferIndex = (x + (dim.width * y)) * 4;
                int r = buffer.get(bufferIndex) & 0xFF;
                int g = buffer.get(bufferIndex + 1) & 0xFF;
                int b = buffer.get(bufferIndex + 2) & 0xFF;
                int a = buffer.get(bufferIndex + 3) & 0xFF;
                int argb = (a << 24) | (r << 16) | (g << 8) | b;
                image.setRGB(x, dim.height - y - 1, argb);
            }
        }

        // Create folder within game_output folder
        File dir = new File(absolutePath, folderName);

        if (!dir.exists()) {
            dir.mkdirs();
        }

        // Create subfolder within the action folder
        File subfolder = createSubfolders(dir);

        if(screenshotCounter == 1) {
            setIndex = getSetIndex(subfolder.getPath());
        }
        System.out.println("Set index for directory: " + subfolder.getPath() + ", " + setIndex);

        File setFolder = new File(subfolder, "set" + setIndex);
        System.out.println(setFolder.getPath());

        if (!setFolder.exists()) {
            setFolder.mkdirs();
        }

        // Save the screenshot with a sequentially numbered filename
        File screenshotFile = new File(setFolder, "screenshot_" + screenshotCounter + ".png");
        screenshotCounter++;

        try {
            ImageIO.write(image, "png", screenshotFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private File createSubfolders(File dir) {
        // Array of subfolder names
        String[] subfolders = {"align_with_tree", "move_to_tree", "break_tree", "success"};

        // Check if the index is within bounds
        if (index < 0 || index >= subfolders.length) {
            if (index >= subfolders.length) {
                index = 0;
            } else {
                throw new IllegalArgumentException("Invalid index: " + index);
            }
        }

        // Create subfolder path
        File subfolder = new File(dir, subfolders[index]);

        System.out.println(subfolders[index]);

        // Create subfolder if it does not exist
        if (!subfolder.exists()) {
            subfolder.mkdirs();
        }

        return subfolder;
    }

    public int getSetIndex(String directoryPath) {
        File directory = new File(directoryPath);

        // Ensure the directory exists
        if (!directory.exists()) {
            throw new IllegalArgumentException("Directory does not exist: " + directoryPath);
        }

        // List files in the directory
        String[] files = directory.list();

        // Filter files that match the "set" prefix and a number pattern
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
}