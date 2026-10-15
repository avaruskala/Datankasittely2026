def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """

    people = [
        {
            "phone": person["phone"][-2:],
            "email": f"@{person['email'].split('@')[1]}",
            "name": person["name"],
        }
        for person in people
    ]

    return people
