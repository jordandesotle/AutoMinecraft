package com.jordandesotle.autominecraft;

import com.jordandesotle.autominecraft.capture.LiveCapture;
import com.mojang.logging.LogUtils;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.slf4j.Logger;

import com.jordandesotle.autominecraft.capture.CaptureScreen;

@Mod(AutoMinecraft.MODID)
public class AutoMinecraft {
    public static final String MODID = "autominecraft";
    private static final Logger LOGGER = LogUtils.getLogger();

    public AutoMinecraft() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();

        modEventBus.addListener(this::commonSetup);

        MinecraftForge.EVENT_BUS.register(this);
        // MinecraftForge.EVENT_BUS.register(new CaptureScreen());
        MinecraftForge.EVENT_BUS.register(new LiveCapture());


        System.out.println("AutoMinecraft: Hello World!");
        System.out.println("Reigstered CaptureScreen");

    }

    private void commonSetup(final FMLCommonSetupEvent event) {

    }


    @Mod.EventBusSubscriber(modid = MODID, bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
    public static class ClientModEvents {
        @SubscribeEvent
        public static void onClientSetup(FMLClientSetupEvent event) {
            System.out.println("OnClientSetup: Hello World!");
        }
    }
}
