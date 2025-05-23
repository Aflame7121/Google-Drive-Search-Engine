import pytest
from WorkerThreads.IndexerWorker import IndexerWorker

class TestIndexerWorker:
    def test_indexer_worker_initialization(self):
        """Test basic initialization of IndexerWorker."""
        worker = IndexerWorker()
        assert worker is not None
        
    def test_indexer_worker_interface(self):
        """Verify basic interface methods exist."""
        worker = IndexerWorker()
        assert hasattr(worker, 'run'), "IndexerWorker should have a run method"