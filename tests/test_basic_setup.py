def test_pytest_configuration():
    """Basic test to verify pytest configuration works."""
    assert True, "Pytest configuration is working correctly"

def test_project_environment(project_root):
    """Verify project root fixture is working."""
    import os
    assert os.path.exists(project_root), "Project root path is valid"