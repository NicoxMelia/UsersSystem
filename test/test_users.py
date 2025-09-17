import pytest
from validators import validate_user
from user_service import register_user
from db import init_db

@pytest.fixture(autouse=True)
def setup_db(tmp_path, monkeypatch):
    import db
    test_db = tmp_path / "test_users.db"
    monkeypatch.setattr(db, "DB_NAME", str(test_db))
    db.init_db()

def test_validate_user_valid():
    valid, msg = validate_user("Juan123", "juan@test.com", 25)
    assert valid is True

def test_validate_user_short_username():
    valid, msg = validate_user("ab", "test@test.com", 20)
    assert valid is False

def test_register_user_and_duplicate():
    success, msg = register_user("Pedro99", "pedro@test.com", 30)
    assert success is True

    success, msg = register_user("Pedro99", "otro@test.com", 40)
    assert success is False
