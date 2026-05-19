from src.user_utils import get_user, is_admin, format_user_name

def test_get_user():
    user = get_user(1)
    assert user["name"] == "Venkatesh"

def test_unknown_user():
    assert get_user(99) is None

def test_not_admin():
    user = get_user(1)
    assert is_admin(user) == False

def test_format_name():
    user = get_user(1)
    assert format_user_name(user) == "Venkatesh (developer)"
