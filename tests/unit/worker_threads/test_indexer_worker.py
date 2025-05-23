import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def test_indexer_worker_import():
    """Test ability to import IndexerWorker."""
    try:
        from WorkerThreads.IndexerWorker import IndexerWorker
        assert True
    except ImportError:
        pytest.fail("Could not import IndexerWorker")

def test_indexer_worker_attributes():
    """Verify basic attributes of IndexerWorker."""
    from WorkerThreads.IndexerWorker import IndexerWorker
    worker = IndexerWorker()
    assert hasattr(worker, 'run'), "IndexerWorker should have a run method"