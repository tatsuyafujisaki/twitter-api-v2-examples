import json
import os

import requests

bearer_token = os.environ.get("BEARER_TOKEN")
query = f"Hello world"


def get_tweets():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/recent",
        headers={"Authorization": f"Bearer {bearer_token}"},
        params={"query": query},
    )

    print(
        json.dumps(response.json(), indent=2, sort_keys=True)
        if response.status_code == 200
        else f"{response.status_code}: {response.text}"
    )


def main():
    get_tweets()


if __name__ == "__main__":
    main()
