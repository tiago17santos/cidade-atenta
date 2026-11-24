
from core.mongodb import get_database


def get_collections():
    db = get_database()

    return {
        "users": db["users"],
        "categories": db["categories"],
        "reports": db["reports"],
        "comments": db["comments"],
        "status_history": db["status_history"],
    }
