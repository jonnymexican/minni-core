import requests
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"

MEMORY_FILE = Path(
    "../data/jon_memories.txt"
)

with open(MEMORY_FILE) as f:
    memories = [
        line.strip()
        for line in f.readlines()
        if line.strip()
    ]

for memory in memories:

    response = requests.post(
        f"{BASE_URL}/remember",
        json={
            "user_id": "jon",
            "content": memory
        }
    )

    print(
        response.status_code,
        memory
    )

print(
    f"Loaded {len(memories)} memories."
)
