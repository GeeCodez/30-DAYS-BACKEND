import json 

def load_json(json_string: str):
    """converts a JSON string into a python dictionary.
    Raises a valueError if the json is invalid"""

    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError (f"Invalid json: {e}")

def save_json(data: dict, indent: int=4) -> str:
    """converts a python dictionary into a json string"""
    return json.dumps(data,indent=indent)

    