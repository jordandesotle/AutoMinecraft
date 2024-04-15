package com.jordandesotle.autominecraft.capture;

import com.jordandesotle.autominecraft.utils.DirectoryManager;

import com.jordandesotle.autominecraft.utils.ImageServer;
import com.jordandesotle.autominecraft.utils.LiveExportManager;
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
import java.nio.file.Path;

import static org.lwjgl.opengl.GL11.*;

public class LiveCapture {

    LiveExportManager manager;
    ImageServer server = new ImageServer(12345);

    private boolean takeScreenshots = false;            // toggled by the "K" key

    private int frameCount = 0;                         // keeps track of how many frames have passed
    private int screenshotCounter = 1;                  // the number that gets added to the end of each screenshot

    private static final int BPP = 4;
    private static final int TYPE = GL_UNSIGNED_BYTE;
    private static final int FORMAT = GL_RGBA;
    private static final Minecraft MC = Minecraft.getInstance();
    private final Dimension dim;


    public LiveCapture() {

        // Creates and manages all needed folders
        manager = new LiveExportManager();              // manager for exporting data to input folder for live demo

        dim = getCurrentDimension();

        // start server for communication to neural network
        server.startServer();

    }

    private Dimension getCurrentDimension() {
        return new Dimension(MC.getWindow().getWidth(), MC.getWindow().getHeight());
    }

    @SubscribeEvent
    public void onRenderTick(TickEvent.RenderTickEvent event) {
        if (event.phase == TickEvent.Phase.END) {
            if (MC.player != null && !MC.isPaused() && takeScreenshots) {
                frameCount++;
                if (frameCount % 300 == 0) {
                    String path = captureScreenshot();

                    // send path name in socket
                    server.sendMessage(server.getClientSocket(), path);
                }
            }
        }
    }

    @SubscribeEvent
    public void onKeyInput(InputEvent.Key event) {
        if (event.getAction() == GLFW.GLFW_PRESS) {
            if (event.getKey() == GLFW.GLFW_KEY_K) {

                takeScreenshots = !takeScreenshots;
                System.out.println("takeScreenshots is now: " + takeScreenshots);
            }
        }
    }

    public String captureScreenshot() {
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

        // Gets the folder to save images to
        File saveDir = manager.getSavePath();

        File screenshotFile = new File(saveDir, "screenshot_" + screenshotCounter + ".png");
        screenshotCounter++;

        System.out.println(screenshotFile.getPath());

        try {
            ImageIO.write(image, "png", screenshotFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        return screenshotFile.getPath();
    }


}