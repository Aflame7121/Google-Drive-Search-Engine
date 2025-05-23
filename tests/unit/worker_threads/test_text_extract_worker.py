import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def test_text_extract_worker_import():
    """Test ability to import TextExtractWorker."""
    try:
        from WorkerThreads.TextExtractWorker import TextExtractWorker
        assert True
    except ImportError:
        pytest.fail("Could not import TextExtractWorker")

def test_text_extract_worker_attributes():
    """Verify basic attributes of TextExtractWorker."""
    from WorkerThreads.TextExtractWorker import TextExtractWorker
    worker = TextExtractWorker()
    assert hasattr(worker, 'run'), "TextExtractWorker should have a run method"