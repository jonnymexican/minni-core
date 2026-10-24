import requests
import json

BASE_URL = "http://127.0.0.1:8000"

USER_ID = "john"


def divider(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def remember(content):

    response = requests.post(
        f"{BASE_URL}/remember",
        json={
            "user_id": USER_ID,
            "content": content
        }
    )

    return response.json()


def recall(query):

    response = requests.post(
        f"{BASE_URL}/recall",
        json={
            "user_id": USER_ID,
            "query": query
        }
    )

    return response.json()


def profile():

    response = requests.get(
        f"{BASE_URL}/profile/{USER_ID}"
    )

    return response.json()


def context(query):

    response = requests.post(
        f"{BASE_URL}/context",
        json={
            "user_id": USER_ID,
            "query": query
        }
    )

    return response.json()


# -------------------------------
# DEMO
# -------------------------------

divider("STORE MEMORIES")

print(
    remember(
        "I love Python"
    )
)

print(
    remember(
        "I'm learning AI"
    )
)

print(
    remember(
        "I'm building Minni"
    )
)


divider("RECALL")

result = recall(
    "Python"
)

print(
    json.dumps(
        result,
        indent=2
    )
)


divider("PROFILE")

result = profile()

print(
    json.dumps(
        result,
        indent=2
    )
)


divider("CONTEXT")

result = context(
    "startup ideas"
)

print(
    json.dumps(
        result,
        indent=2
    )
)
