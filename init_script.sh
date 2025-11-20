#!/bin/bash

# Create virtual environment
python3 -m venv env

# Activate the environment
source env/bin/activate

# Install packages (if you have any in requirements.txt)
pip install -r requirements.txt

# Freeze requirements
pip freeze > project_library.txt

echo "Environment created and activated."
echo "requirements.txt generated."
