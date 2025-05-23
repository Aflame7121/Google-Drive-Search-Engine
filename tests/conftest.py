import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="session")
def project_root():
    """Fixture providing the project's root directory path."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture
def mock_env(monkeypatch):
    """Fixture to help mock environment variables and configurations."""
    def _set_env(key, value):
        monkeypatch.setenv(key, value)
    return _set_env