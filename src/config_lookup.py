def find_key(data, key):
    """
    Depth-first left-to-right search for the first occurrence of key.
    Return value or None if not found.
    """

    # Case 1: If data is a dictionary
    if isinstance(data, dict):
        # Check if the key exists at this level
        if key in data:
            return data[key]
        # Otherwise, search recursively in the values
        for value in data.values():
            result = find_key(value, key)
            if result is not None:
                return result

    # Case 2: If data is a list or tuple, search each element
    elif isinstance(data, (list, tuple)):
        for item in data:
            result = find_key(item, key)
            if result is not None:
                return result

    # Case 3: For other data types, do nothing
    return None
