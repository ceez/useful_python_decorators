import functools


def require_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError(f"{user['name']} lacks {role} privileges")
            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@require_role("admin")
def delete_user(user, user_id):
    print(f"{user['name']} deleted user {user_id}")


admin = {"name": "Jane", "role": "admin"}
guest = {"name": "Bob", "role": "guest"}

delete_user(admin, 42)
# Jane deleted user 42
delete_user(guest, 42)
# PermissionError: Bob lacks admin privileges
