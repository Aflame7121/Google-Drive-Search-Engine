import json
from typing import Dict, Optional

class MockAuthManager:
    """
    Mock authentication manager for testing authentication functions.
    Simulates credential loading and validation without actual external dependencies.
    """
    def __init__(self, client_id_path: str = '.auth/client_id.json', 
                 credentials_path: str = '.auth/credentials.json'):
        """
        Initialize mock authentication manager with configurable paths.
        
        Args:
            client_id_path (str): Path to client ID configuration
            credentials_path (str): Path to credentials configuration
        """
        self.client_id_path = client_id_path
        self.credentials_path = credentials_path
    
    def load_client_id(self) -> Optional[Dict[str, str]]:
        """
        Load client ID configuration with error handling.
        
        Returns:
            Optional dictionary of client ID configuration
        """
        try:
            with open(self.client_id_path, 'r') as f:
                data = json.load(f)
                return data.get('web', {})
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
    
    def load_credentials(self) -> Optional[Dict[str, str]]:
        """
        Load credentials configuration with error handling.
        
        Returns:
            Optional dictionary of credentials
        """
        try:
            with open(self.credentials_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
    
    def validate_credentials(self) -> bool:
        """
        Validate loaded credentials.
        
        Returns:
            Boolean indicating credential validity
        """
        client_id = self.load_client_id()
        credentials = self.load_credentials()
        
        return (client_id is not None and 
                credentials is not None and 
                'client_id' in client_id and 
                'refresh_token' in credentials)