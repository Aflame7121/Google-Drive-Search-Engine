"""
Unit tests for the TextExtractWorker module.

This module contains tests to validate the functionality of the TextExtractWorker.
"""

import pytest
from WorkerThreads.TextExtractWorker import TextExtractWorker

@pytest.mark.unit
def test_text_extract_worker_initialization():
    """
    Test the initialization of the TextExtractWorker.
    
    Ensures that the TextExtractWorker can be created without errors.
    """
    worker = TextExtractWorker()
    assert worker is not None