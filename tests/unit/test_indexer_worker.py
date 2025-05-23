"""
Unit tests for the IndexerWorker module.

This module contains tests to validate the functionality of the IndexerWorker.
"""

import pytest
from WorkerThreads.IndexerWorker import IndexerWorker

@pytest.mark.unit
def test_indexer_worker_initialization():
    """
    Test the initialization of the IndexerWorker.
    
    Ensures that the IndexerWorker can be created without errors.
    """
    worker = IndexerWorker()
    assert worker is not None