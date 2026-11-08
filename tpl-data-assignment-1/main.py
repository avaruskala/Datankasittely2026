from project.api import fetch_users
from project.data_analysis import analyse_users
from project.data_protection import anonymize_users, mask_users


def main():
    users = fetch_users()
    mask_users(users)
    anonymize_users(users)
    analyse_users(users)


if __name__ == "__main__":
    main()
