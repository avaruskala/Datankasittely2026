from datetime import datetime


def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """

    for person in people:
        person["city_initial"] = person["city"][0]
        person["birth_year"] = int(person["birthdate"].split("-")[0])
        del person["name"]
        del person["birthdate"]
        del person["city"]

    return people

