#!/bin/bash

echo "🧪 Setting up Python 3.12 virtual environment..."

# Check for python3.12
if ! command -v python3.12 &> /dev/null
then
    echo "❌ Python 3.12 not found."
    echo "👉 Install it using: sudo dnf install python3.12 python3.12-virtualenv"
    exit 1
fi

# Create venv
python3.12 -m venv .venv
if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment."
    exit 1
fi

# Activate venv
source .venv/bin/activate

# Upgrade pip & install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ All set! Venv created with Python 3.12 and dependencies installed."
echo "💡 To activate later: source .venv/bin/activate"u