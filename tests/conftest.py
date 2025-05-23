"""
Pytest configuration file for the project.
This file helps configure global pytest settings and provides shared fixtures.
"""
import pytest
import sys
import os

# Ensure the project root directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))