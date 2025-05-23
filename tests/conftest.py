import pytest
import sys
import os

# Ensure project root is in Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

@pytest.fixture(scope="session")
def project_root():
    """Fixture providing the project's root directory path."""
    return PROJECT_ROOT

@pytest.fixture
def mock_env(monkeypatch):
    """Fixture to help mock environment variables and configurations."""
    def _set_env(key, value):
        monkeypatch.setenv(key, value)
    return _set_env

@pytest.fixture
def sys_path_includes_project():
    """Ensure project root is in sys.path for import resolution."""
    original_path = sys.path.copy()
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    
    yield
    
    # Restore original sys.path after test
    sys.path = original_path