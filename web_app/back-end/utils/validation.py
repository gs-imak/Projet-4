def validate_query(data):
    if not isinstance(data, dict) or "query" not in data:
        return False, {"error": "Invalid query format"}
    return True, None
