package com.jordandesotle.autominecraft.capture;

import com.jordandesotle.autominecraft.utils.DirectoryManager;

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

import static org.lwjgl.opengl.GL11.*;

public class CaptureScreen {


    DirectoryManager dirManager;


    private boolean takeScreenshots = false;            // toggled by the "K" key
    private int subFolderIndex = 0;                     // represents which folder is currently being recorded to
    private int setIndex = 0;                           // increases once all subfolders have been written to

    private int frameCount = 0;                         // keeps track of how many frames have passed
    private int screenshotCounter = 1;                  // the number that gets added to the end of each screenshot

    private static final int BPP = 4;
    private static final int TYPE = GL_UNSIGNED_BYTE;
    private static final int FORMAT = GL_RGBA;
    private static final Minecraft MC = Minecraft.getInstance();
    private final Dimension dim;

    public CaptureScreen() {

        // Creates and manages all needed folders
        dirManager = new DirectoryManager();

        dim = getCurrentDimension();
    }

    private Dimension getCurrentDimension() {
        return new Dimension(MC.getWindow().getWidth(), MC.getWindow().getHeight());
    }

    @SubscribeEvent
    public void onRenderTick(TickEvent.RenderTickEvent event) {
        if (event.phase == TickEvent.Phase.END) {
            if (MC.player != null && !MC.isPaused() && takeScreenshots) {
                frameCount++;
                if (frameCount % 30 == 0) {
                    captureScreenshot();
                }
            }
        }
    }

    @SubscribeEvent
    public void onKeyInput(InputEvent.Key event) {
        if (event.getAction() == GLFW.GLFW_PRESS) {
            if (event.getKey() == GLFW.GLFW_KEY_K) {
                if (takeScreenshots) {
                    subFolderIndex = (subFolderIndex + 1) % dirManager.getNumSubActions();
                    screenshotCounter = 1;
                }
                takeScreenshots = !takeScreenshots;
                System.out.println("takeScreenshots is now: " + takeScreenshots);
            }
        }
    }

    public void captureScreenshot() {
        System.out.println("Screenshot triggered");

        int bufferSize = dim.height * dim.width * BPP;
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

        // Gets the folder based on the current index to save image "sets" to
        File saveDir = dirManager.getSavePath(subFolderIndex);

        if (screenshotCounter == 1) {
            setIndex = dirManager.getSetIndex(saveDir.getPath());
        }

        File setFolder = new File(saveDir, "set" + setIndex);
        dirManager.createDirectoryIfNotExist(setFolder);
        System.out.println("Set index for directory: " + saveDir.getPath() + ", " + setIndex);


        File screenshotFile = new File(setFolder, "screenshot_" + screenshotCounter + ".png");
        screenshotCounter++;

        try {
            ImageIO.write(image, "png", screenshotFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }


}
