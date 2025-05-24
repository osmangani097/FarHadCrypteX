#!/bin/bash

apt update && apt upgrade -y
apt install python -y
apt install git -y
rm -rf FarHadCrypteX
git clone https://github.com/osmangani097/FarHadCrypteX
cd FarHadCrypteX


ulimit -n 999999
chmod 777 *


git pull


python3 FarHadCrypteX.py
