import pytest
from WorkerThreads.DownloadWorker import DownloadWorker

class TestDownloadWorker:
    def test_download_worker_initialization(self):
        """Test basic initialization of DownloadWorker."""
        worker = DownloadWorker()
        assert worker is not None
        
    def test_download_worker_interface(self):
        """Verify basic interface methods exist."""
        worker = DownloadWorker()
        assert hasattr(worker, 'run'), "DownloadWorker should have a run method"