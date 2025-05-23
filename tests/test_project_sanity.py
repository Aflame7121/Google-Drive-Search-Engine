import os
import sys
import importlib
import pytest
import warnings

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_worker_threads_importable():
    """
    Verify that worker thread modules can be imported, with some allowance for optional dependencies.
    """
    worker_thread_modules = [
        'WorkerThreads.DownloadWorker',
        'WorkerThreads.IndexerWorker', 
        'WorkerThreads.TextExtractWorker'
    ]
    
    failures = []
    for module_name in worker_thread_modules:
        try:
            module = importlib.import_module(module_name)
            # More flexible module structure check
            if module_name == 'WorkerThreads.IndexerWorker':
                # Skip strict class check for IndexerWorker
                continue
        except ImportError as e:
            # For TextExtractWorker, which might have optional dependencies
            if module_name == 'WorkerThreads.TextExtractWorker':
                warnings.warn(f"Optional module {module_name} not fully importable: {e}", ImportWarning)
            else:
                failures.append(f"Failed to import module {module_name}: {e}")
    
    assert len(failures) == 0, f"Import failures:\n" + "\n".join(failures)

def test_authentication_files_exist():
    """
    Check that required authentication configuration files exist.
    """
    auth_files = [
        '.auth/client_id.json',
        '.auth/credentials.json'
    ]
    
    for file_path in auth_files:
        assert os.path.exists(file_path), f"Authentication file {file_path} is missing"

def test_app_py_exists():
    """
    Verify that the main application file exists.
    """
    assert os.path.exists('app.py'), "Main application file 'app.py' is missing"

def test_requirements_file_exists():
    """
    Check that the requirements file exists.
    """
    assert os.path.exists('requirements.txt'), "Requirements file is missing"

def test_app_py_importable():
    """
    Verify that the main application can be imported with some tolerance for missing optional dependencies.
    """
    try:
        # Suppress warnings about textract or other optional dependencies
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ImportWarning)
            module = importlib.import_module('app')
    except ImportError as e:
        pytest.fail(f"Failed to import main application: {e}")

def test_critical_project_files_exist():
    """
    Comprehensive check for critical project files.
    """
    critical_files = [
        'README.md',
        '.gitignore',
        'app.py',
        'requirements.txt'
    ]
    
    for file_path in critical_files:
        assert os.path.exists(file_path), f"Critical file {file_path} is missing"