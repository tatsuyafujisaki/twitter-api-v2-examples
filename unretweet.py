import json
import os

from requests_oauthlib import OAuth1Session

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
user_id = ""
tweet_id = ""


def main():
    oauth = OAuth1Session(
        client_key=consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    response = oauth.delete(
        f"https://api.twitter.com/2/users/{user_id}/retweets/{tweet_id}"
    )

    print(
        json.dumps(response.json(), indent=2, sort_keys=True)
        if response.status_code == 200
        else f"{response.status_code}: {response.text}"
    )


if __name__ == "__main__":
    main()
