from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by restoring mutable in-memory data after each test."""
    original = deepcopy(app_module.activities)
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original))

    yield

    app_module.activities.clear()
    app_module.activities.update(original)


@pytest.fixture
def client():
    return TestClient(app_module.app)
