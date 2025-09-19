#!/bin/bash

echo "Building Repository Cloner Executable..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not found in PATH."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not available."
    echo "Please ensure pip3 is installed with Python."
    exit 1
fi

echo "Installing PyInstaller..."
pip3 install pyinstaller

echo
echo "Building executable..."
pyinstaller --onefile --console --name "RepoCloner" repo_cloner.py

if [ $? -ne 0 ]; then
    echo
    echo "Error: Failed to build executable."
    exit 1
fi

echo
echo "Build completed successfully!"
echo
echo "The executable has been created in the 'dist' folder."
echo "You can copy 'dist/RepoCloner' to any location on your system."
echo
echo "Note: The executable requires Git to be installed on the target system."
echo

# Copy the executable to the current directory for convenience
cp "dist/RepoCloner" "RepoCloner" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Executable also copied to current directory as 'RepoCloner'"
fi

echo
