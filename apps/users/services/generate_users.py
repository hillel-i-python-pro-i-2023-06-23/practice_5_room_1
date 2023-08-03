from collections.abc import Iterator

from apps.users.models import User
from apps.users.services import faker


def generate_user() -> User:
    return User(
        name=faker.unique.username(),
        email=faker.unique.company_email(),
        password=faker.unique.password()
    )


def generate_users(amount: int) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
