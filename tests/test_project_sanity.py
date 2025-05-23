import os
import importlib
import pytest

def test_worker_threads_importable():
    """
    Verify that all worker thread modules can be imported without errors.
    """
    worker_thread_modules = [
        'WorkerThreads.DownloadWorker',
        'WorkerThreads.IndexerWorker', 
        'WorkerThreads.TextExtractWorker'
    ]
    
    for module_name in worker_thread_modules:
        try:
            importlib.import_module(module_name)
        except ImportError as e:
            pytest.fail(f"Failed to import module {module_name}: {e}")

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
    Verify that the main application can be imported without errors.
    """
    try:
        importlib.import_module('app')
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