from project.api import fetch_users
from project.data_analysis import analyse_users
from project.data_protection import anonymize_users, mask_users


def main():
    # Fetch and store
    users = fetch_users()
    # Data protection
    mask_users(users)
    anonymize_users(users)
    # Analyse and print
    analyse_users(users)


if __name__ == "__main__":
    main()
