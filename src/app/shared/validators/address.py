from jsonschema import validate, ValidationError


VALIDATE_ADDRESS_SCHEMA = {
    "type": "object",
    "required": [
        "street",
        "number",
        "city",
        "state",
        "zip_code",
    ],
    "properties": {
        "street": {"type": "string"},
        "number": {"type": "string"},
        "complement": {"type": "string"},
        "neighborhood": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "zip_code": {"type": "string"},
        "country": {"type": "string"},
    },
}


def validate_address(value):
    if not isinstance(value, dict):
        raise ValidationError("Address must be a JSON object")

    try:
        validate(
            instance=value,
            schema=VALIDATE_ADDRESS_SCHEMA,
            cls=ValidationError,
        )

    except ValidationError as e:
        raise ValidationError(f"Invalid address format: {e.message}")
