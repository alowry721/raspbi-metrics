#!/bin/bash

wget https://gist.githubusercontent.com/vsajip/4673395/raw/0504ce930e6dc6b02e4955a07d91ad462e0ba80b/pyvenvex.py

sudo apt-get install python3-pip

python3 pyvenvex.py py3_venv

source py3_venv/bin/activate

echo "alias py3-venv='source py3_venv/bin/activate'" >> ~/.bash_profile

. .bash_profile
py3-venv

sudo apt-get install python3-dev
pip install psutil
pip install gpiozero