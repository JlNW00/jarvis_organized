#!/bin/bash

# Run tests for Jarvis AI Assistant
echo "Running Jarvis AI Assistant tests..."

# Create __init__.py files to make directories importable
touch /home/ubuntu/jarvis_project/tests/__init__.py
touch /home/ubuntu/jarvis_project/core/__init__.py

# Run the tests
cd /home/ubuntu/jarvis_project
python3 -m unittest tests/test_jarvis.py

echo "Tests completed."
