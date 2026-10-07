import pandas as pd
from client.api_client import fetch_data
from utils.validators import validate_items


def main():
    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Fetching paginated data…")
    # Fetch items
    data = fetch_data(api_url)
    df = pd.DataFrame(data)

    if data is not None:
        print("Validating items…")
        # Validate items
        if not validate_items(data):
            raise ValueError("Items no valid")

        json_file_path = "data/posts.json"
        # Save JSON data into the file
        df.to_json(json_file_path)


if __name__ == "__main__":
    main()
