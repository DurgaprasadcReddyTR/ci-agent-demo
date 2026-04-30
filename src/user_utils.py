def get_user(user_id):
    users = {
        1: {"name": "Venkatesh", "role": "developer"},
        2: {"name": "Priya",     "role": "devops"}
    }
    return users[user_id]

def is_admin(user):
    if not user:
        return False
    return user.get("role") == "admin"

def format_user_name(user):
    return user["name"].upper() + " (" + user["role"] + ")"

