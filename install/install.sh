#!/bin/bash

# Detect the operating system
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    source utils/linux_utils.sh
elif [[ "$OSTYPE" == "darwin"* ]]; then
    source utils/mac_utils.sh
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source utils/windows_utils.bat
else
    echo "Unsupported operating system."
    exit 1
fi

# Continue with the rest of your installation steps
echo "Common installation steps..."
# Unpackaging Minecraft server, setting up mod development, configuring neural network, etc.
