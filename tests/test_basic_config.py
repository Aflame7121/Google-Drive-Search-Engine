import os
import pytest

def test_project_structure(project_root):
    """
    Verify basic project configuration
    """
    assert os.path.exists(project_root), "Project root directory should exist"
    assert os.path.exists(os.path.join(project_root, 'app.py')), "Main application file should exist"

@pytest.mark.unit
def test_pytest_markers():
    """
    Ensure pytest can recognize custom markers
    """
    assert True, "Unit marker test should pass"