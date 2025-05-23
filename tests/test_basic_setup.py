import os
import sys

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

def test_worker_threads_imports():
    """Verify that Worker Thread modules can be imported."""
    try:
        from WorkerThreads.DownloadWorker import DownloadWorker
        from WorkerThreads.IndexerWorker import IndexerWorker
        from WorkerThreads.TextExtractWorker import TextExtractWorker
        assert True, "All worker thread modules can be imported"
    except ImportError as e:
        assert False, f"Failed to import worker thread modules: {e}"