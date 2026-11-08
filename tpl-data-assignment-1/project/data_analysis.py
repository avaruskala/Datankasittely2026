from project.database import User
import pandas as pd


def analyse_users(users: list[User]):
    """Analyse users by printing shape first two and last two"""
    df = pd.DataFrame(
        data=[
            {"id": user.id, "Name": user.name, "Email": user.email, "Phone": user.phone}
            for user in users
        ],
    )

    print(df.shape)
    print("First two")
    print(df.head(2))
    print("Last two")
    print(df.tail(2))
