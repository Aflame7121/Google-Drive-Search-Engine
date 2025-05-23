import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def mock_config():
    """Fixture to provide mock configuration for tests."""
    return {
        'auth_path': '.auth',
        'download_path': 'downloads',
        'index_path': 'index'
    }