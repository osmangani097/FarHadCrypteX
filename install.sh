#!/bin/bash

# Installing dependencies
apt update && apt upgrade -y
apt install python -y
apt install git -y

# Cloning the repository (replace with your own GitHub repo if available)
rm -rf FarHadCrypteX
git clone https://github.com/YourGitHubUsername/FarHadCrypteX
cd FarHadCrypteX

# Setting permissions
ulimit -n 999999
chmod 777 *

# Pulling latest updates
git pull

# Running the tool
python3 farhad.py
