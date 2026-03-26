from src.user_utils import get_user, is_admin

def test_get_user():
    user = get_user(1)
    assert user["name"] == "Venkatesh"

def test_unknown_user():
    assert get_user(99) is None

def test_not_admin():
    user = get_user(1)
    assert is_admin(user) == False
