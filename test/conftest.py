"""Config for tests."""
import pytest
from app import create_app


@pytest.fixture
def app():
    """Return app."""
    app = create_app()
    app.app_context().push()
    return app
