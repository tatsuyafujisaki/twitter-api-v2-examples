import json
import os

import requests

bearer_token = os.environ.get("BEARER_TOKEN")
user_id = ""


def main():
    response = requests.get(
        f"https://api.twitter.com/2/users/{user_id}",
        headers={"Authorization": f"Bearer {bearer_token}"},
    )

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    print(
        json.dumps(response.json(), indent=2, sort_keys=True)
        if response.status_code == 200
        else f"{response.status_code}: {response.text}"
    )


if __name__ == "__main__":
    main()
