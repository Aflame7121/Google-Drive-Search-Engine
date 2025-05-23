import os
import sys
import pytest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure(config):
    """
    Configure pytest settings and add custom markers
    """
    config.addinivalue_line(
        "markers", 
        "unit: mark a test as a unit test"
    )
    config.addinivalue_line(
        "markers", 
        "integration: mark a test as an integration test"
    )

@pytest.fixture(scope='session')
def project_root():
    """
    Fixture to provide the project root directory path
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))