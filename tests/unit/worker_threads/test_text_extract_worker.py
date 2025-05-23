import pytest
from WorkerThreads.TextExtractWorker import TextExtractWorker

class TestTextExtractWorker:
    def test_text_extract_worker_initialization(self):
        """Test basic initialization of TextExtractWorker."""
        worker = TextExtractWorker()
        assert worker is not None
        
    def test_text_extract_worker_interface(self):
        """Verify basic interface methods exist."""
        worker = TextExtractWorker()
        assert hasattr(worker, 'run'), "TextExtractWorker should have a run method"