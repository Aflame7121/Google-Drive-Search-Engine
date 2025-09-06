"""
Unit tests for the DownloadWorker module.

This module contains tests to validate the functionality of the DownloadWorker.
"""

import pytest
from WorkerThreads.DownloadWorker import DownloadWorker

@pytest.mark.unit
def test_download_worker_initialization():
    """
    Test the initialization of the DownloadWorker.
    
    Ensures that the DownloadWorker can be created without errors.
    """
    worker = DownloadWorker()
    assert worker is not None