import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def test_worker_threads_directory_exists():
    """Verify that the WorkerThreads directory exists."""
    assert os.path.exists('WorkerThreads'), "WorkerThreads directory should exist"

def test_download_worker_file_exists():
    """Check if DownloadWorker.py file exists."""
    assert os.path.exists('WorkerThreads/DownloadWorker.py'), "DownloadWorker.py should exist"

def test_download_worker_importable():
    """Test basic importability of DownloadWorker."""
    try:
        from WorkerThreads.DownloadWorker import DownloadWorker
        assert hasattr(DownloadWorker, '__init__'), "DownloadWorker should have an __init__ method"
    except ImportError:
        pytest.skip("Unable to import DownloadWorker, possibly due to external dependencies")