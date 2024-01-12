package com.jordandesotle.autominecraft.utils;

import net.minecraft.client.Minecraft;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

import org.lwjgl.BufferUtils;
import org.lwjgl.opengl.GL11;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.text.SimpleDateFormat;
import java.util.Date;

import static org.lwjgl.opengl.GL11.*;


public class CaptureScreen {

    // Specify the absolute directory path
    String absolutePath = "/home/jordan/Documents/AutoMinecraft_Root/nueral_network/data/game_output";
    String folderName = "";

    private static final int BPP = 4; // bytes per pixel (RGBA)
    private static final int TYPE = GL_UNSIGNED_BYTE;
    private static final int FORMAT = GL_RGBA;
    private static final Minecraft MC = Minecraft.getInstance();

    private final Dimension dim;

    private int frameCount = 0;
    private int screenshotCounter = 1;

    public CaptureScreen() {
        folderName = createSessionName();
        System.out.println("Created folder name: " + folderName);

        dim = getCurrentDimension();
    }

    private Dimension getCurrentDimension() {
        return new Dimension(MC.getWindow().getWidth(), MC.getWindow().getHeight());
    }

    @SubscribeEvent
    public void onRenderTick(TickEvent.RenderTickEvent event) {
        if (event.phase == TickEvent.Phase.END) {

            // Only take picutures while in game
            if(MC.player != null && !MC.isPaused()) {

                // Increment frame count on each render tick
                frameCount++;

                // Capture screenshot every 30 frames
                if (frameCount % 30 == 0) {

                    captureScreenshot();
                }
                
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
                int index = (x + (dim.width * y)) * 4;
                int r = buffer.get(index) & 0xFF;
                int g = buffer.get(index + 1) & 0xFF;
                int b = buffer.get(index + 2) & 0xFF;
                int a = buffer.get(index + 3) & 0xFF;
                int argb = (a << 24) | (r << 16) | (g << 8) | b;
                image.setRGB(x, dim.height - y - 1, argb);
            }
        }

        File screenshotsDir = new File(absolutePath, folderName);

        if (!screenshotsDir.exists()) {
            screenshotsDir.mkdirs();
        }

        // Save the screenshot with a sequentially numbered filename
        File screenshotFile = new File(screenshotsDir, "screenshot_" + screenshotCounter + ".png");
        screenshotCounter++;

        try {
            ImageIO.write(image, "png", screenshotFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public String createSessionName() {
        // Create a new folder with a name based on the current timestamp
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMdd_HHmmss");
        String folderName = "session_" + dateFormat.format(new Date());

        return folderName;
    }

}