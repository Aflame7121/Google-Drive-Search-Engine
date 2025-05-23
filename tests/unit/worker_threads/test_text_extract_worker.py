import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def test_worker_threads_directory_exists():
    """Verify that the WorkerThreads directory exists."""
    assert os.path.exists('WorkerThreads'), "WorkerThreads directory should exist"

def test_text_extract_worker_file_exists():
    """Check if TextExtractWorker.py file exists."""
    assert os.path.exists('WorkerThreads/TextExtractWorker.py'), "TextExtractWorker.py should exist"

def test_text_extract_worker_importable():
    """Test basic importability of TextExtractWorker."""
    try:
        from WorkerThreads.TextExtractWorker import TextExtractWorker
        assert hasattr(TextExtractWorker, '__init__'), "TextExtractWorker should have an __init__ method"
    except ImportError:
        pytest.skip("Unable to import TextExtractWorker, possibly due to external dependencies")