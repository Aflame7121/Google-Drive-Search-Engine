import pytest
import json
import os
from tests.auth.mock_auth import MockAuthManager

class TestAuthenticationConfiguration:
    """
    Test suite for authentication configuration and validation.
    """
    
    def setup_method(self):
        """
        Setup method to prepare test environment.
        """
        self.mock_auth_manager = MockAuthManager()
    
    def test_client_id_file_exists(self):
        """
        Test that client ID configuration file exists.
        """
        assert os.path.exists('.auth/client_id.json'), "Client ID file is missing"
    
    def test_credentials_file_exists(self):
        """
        Test that credentials file exists.
        """
        assert os.path.exists('.auth/credentials.json'), "Credentials file is missing"
    
    def test_load_client_id_valid(self):
        """
        Test loading valid client ID configuration.
        """
        client_id = self.mock_auth_manager.load_client_id()
        assert client_id is not None, "Client ID could not be loaded"
        assert 'client_id' in client_id, "Invalid client ID configuration"
    
    def test_load_credentials_valid(self):
        """
        Test loading valid credentials.
        """
        credentials = self.mock_auth_manager.load_credentials()
        assert credentials is not None, "Credentials could not be loaded"
        assert 'refresh_token' in credentials, "Invalid credentials configuration"
    
    def test_validate_credentials(self):
        """
        Test comprehensive credential validation.
        """
        assert self.mock_auth_manager.validate_credentials(), "Credentials validation failed"
    
    @pytest.mark.parametrize("bad_path", [
        '/nonexistent/path/client_id.json',
        '/path/with/invalid/json.json'
    ])
    def test_invalid_path_handling(self, bad_path, monkeypatch):
        """
        Test handling of invalid paths and JSON decoding.
        
        Args:
            bad_path (str): Path to simulate invalid configuration
            monkeypatch: pytest monkeypatch fixture
        """
        monkeypatch.setattr(self.mock_auth_manager, 'client_id_path', bad_path)
        monkeypatch.setattr(self.mock_auth_manager, 'credentials_path', bad_path)
        
        assert self.mock_auth_manager.load_client_id() is None
        assert self.mock_auth_manager.load_credentials() is None
        assert not self.mock_auth_manager.validate_credentials()