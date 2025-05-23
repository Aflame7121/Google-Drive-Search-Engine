"""
Pytest configuration and global fixtures for the Google Drive Search Application.

This module provides shared fixtures, configuration, and utility functions
for testing across different test modules.
"""

import os
import sys
import pytest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure(config):
    """
    Pytest configuration hook for global settings.
    
    Configures project-wide test settings and markers.
    """
    config.addinivalue_line(
        "markers", 
        "unit: mark a test as a unit test for specific component."
    )
    config.addinivalue_line(
        "markers", 
        "integration: mark a test as an integration test."
    )

@pytest.fixture(scope='session')
def project_root():
    """
    Fixture to provide the absolute path to the project root directory.
    
    Returns:
        str: Absolute path to the project root.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture(scope='function')
def temp_directory(tmp_path):
    """
    Fixture to provide a temporary directory for test file operations.
    
    Args:
        tmp_path: Built-in pytest fixture for temporary directory.
    
    Returns:
        Path: A temporary directory path for each test function.
    """
    return tmp_path