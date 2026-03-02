import pytest
from app import app

@pytest.fixture
def client():
    """Configures the app for testing."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Tests the home route."""
    response = client.get('/')
    assert response.status_code == 200
    # Updated to match your "Hello earth!!!!" string
    assert b"Hello earth!!!! - see what SSH did - with versioning this time" in response.data

def test_contact_page(client):
    """Tests the contact route."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact us at email: support@example.com" in response.data