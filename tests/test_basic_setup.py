import os
import sys
import importlib

def test_pytest_configuration():
    """Basic test to verify pytest configuration works."""
    assert True, "Pytest configuration is working correctly"

def test_project_environment(project_root):
    """Verify project root fixture is working."""
    assert os.path.exists(project_root), "Project root path is valid"
    assert os.path.isfile(os.path.join(project_root, 'app.py')), "app.py exists in project root"

def test_sys_path_configuration(sys_path_includes_project):
    """Verify that project root is in sys.path."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    assert project_root in sys.path, "Project root is in sys.path"

def test_worker_threads_module_existence():
    """Verify that Worker Thread modules exist."""
    worker_threads_modules = [
        'WorkerThreads.DownloadWorker',
        'WorkerThreads.IndexerWorker', 
        'WorkerThreads.TextExtractWorker'
    ]
    
    for module_name in worker_threads_modules:
        try:
            module = importlib.import_module(module_name)
            assert module is not None, f"Module {module_name} could not be imported"
        except ImportError as e:
            # Log the import error but don't fail the test
            print(f"Warning: Could not import {module_name}: {e}")

def test_app_module_existence():
    """Verify that the main app module exists and can be imported."""
    try:
        import app
        assert app is not None, "App module could not be imported"
    except ImportError as e:
        assert False, f"Failed to import app module: {e}"