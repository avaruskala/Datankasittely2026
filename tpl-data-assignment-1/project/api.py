import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .configuration import DATABASE_URL
from .database import User

engine = create_engine(DATABASE_URL)
sess = sessionmaker(bind=engine)


def fetch_users() -> list[User]:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    session = sess()
    for u in users:
        user = User(
            id=u["id"],
            name=u["name"],
            username=u["username"],
            email=u["email"],
            phone=u["phone"],
            website=u["website"],
        )
        session.merge(user)
    session.commit()
    users = session.query(User).all()
    session.close()
    print("Users inserted into database.")
    return users
