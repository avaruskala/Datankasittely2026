from project.database import User


def mask_users(users: list[User]):
    for user in users:
        user.phone = user.phone[-2:]


def anonymize_users(users: list[User]):
    for user in users:
        user.name = user.name[0]
