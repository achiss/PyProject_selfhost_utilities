def from_unexpected(description: str | None) -> str:

    if isinstance(description, str):
        return f'unexpected error during verification method - {description}'

    return 'unexpected error during verification method'
