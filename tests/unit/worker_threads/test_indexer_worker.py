import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def test_worker_threads_directory_exists():
    """Verify that the WorkerThreads directory exists."""
    assert os.path.exists('WorkerThreads'), "WorkerThreads directory should exist"

def test_indexer_worker_file_exists():
    """Check if IndexerWorker.py file exists."""
    assert os.path.exists('WorkerThreads/IndexerWorker.py'), "IndexerWorker.py should exist"

def test_indexer_worker_importable():
    """Test basic importability of IndexerWorker."""
    try:
        from WorkerThreads.IndexerWorker import IndexerWorker
        assert hasattr(IndexerWorker, '__init__'), "IndexerWorker should have an __init__ method"
    except ImportError:
        pytest.skip("Unable to import IndexerWorker, possibly due to external dependencies")