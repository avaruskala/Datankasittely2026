import requests
from config import API_URL, DATABASE_URL
from db.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def main():
    response = requests.get(API_URL)
    users = response.json()

    session = SessionLocal()
    for u in users:
        user = User(
            id=u["id"], name=u["name"], username=u["username"], email=u["email"]
        )
        session.merge(user)  # merge avoids duplicate key errors
    session.commit()
    session.close()
    print("Users inserted into database.")


if __name__ == "__main__":
    main()
