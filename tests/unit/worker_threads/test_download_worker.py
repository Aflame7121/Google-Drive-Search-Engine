import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def test_download_worker_import():
    """Test ability to import DownloadWorker."""
    try:
        from WorkerThreads.DownloadWorker import DownloadWorker
        assert True
    except ImportError:
        pytest.fail("Could not import DownloadWorker")

def test_download_worker_attributes():
    """Verify basic attributes of DownloadWorker."""
    from WorkerThreads.DownloadWorker import DownloadWorker
    worker = DownloadWorker()
    assert hasattr(worker, 'run'), "DownloadWorker should have a run method"