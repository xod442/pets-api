schema = {
    "type": "object",
    "properties": {
        "neighborhood":   {"type": "string"},
        "name":           {"type": "string"},
        "street_address": {"type": "string"},
        "city":           {"type": "string"},
        "state":          {"type": "string", "pattern": "^[A-Z]{2}$"},
        "zip":            {"type": "string", "pattern": "^[0-9]{5}$"},
        "phone":          {"type": "string", "pattern": "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"},
        "store_id":       {"type": "string"}
    },
    "required": ["neighborhood", "name", "street_address", "city", "state", "zip", "phone", "store_id"]
}
