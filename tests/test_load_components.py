import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json
from unittest.mock import patch

from backend.load_components import load_json_data

@pytest.fixture
def mock_directory(tmp_path):
    # Create a mock directory and JSON files
    test_dir = tmp_path / 'test_components'
    test_dir.mkdir()

    # Mock JSON data for testing
    json_data = {
        'motor': {'name': 'Motor X', 'thrust': 100},
        'propeller': {'name': 'Prop Y', 'diameter': 5}
    }

    # Create mock files
    with open(test_dir / 'motor_options.json', 'w') as f:
        json.dump(json_data['motor'], f)
    
    with open(test_dir / 'propeller_options.json', 'w') as f:
        json.dump(json_data['propeller'], f)

    yield str(test_dir)

    # Cleanup (optional)
    for file in os.listdir(test_dir):
        os.remove(test_dir / file)
    os.rmdir(test_dir)

def test_load_components_valid(mock_directory):
    # Test valid loading of components
    data = load_json_data(directory=mock_directory)
    print(data)
    assert 'motor' in data
    assert 'propeller' in data
    assert len(data['motor']) == 2
    assert len(data['propeller']) == 2

def test_load_components_empty_directory():
    # Test empty directory
    components = load_json_data(directory='empty_directory')
    
    assert components == {}

def test_load_components_invalid_directory():
    # Test invalid directory
    with patch('os.path.exists', return_value=False):
        components = load_json_data(directory='invalid_directory')
    
    assert components == {}

def test_load_components_json_decode_error(mock_directory):
    # Test JSON decode error (corrupted JSON)
    with open(os.path.join(mock_directory, 'corrupt_options.json'), 'w') as f:
        f.write('{"invalid_json":}')

    components = load_json_data(directory=mock_directory)
    
    assert 'corrupt_options' not in components
