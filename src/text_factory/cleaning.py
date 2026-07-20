def clean_text(text: str) -> str:
    """Normalize text casing and whitespace."""
    lower_text = text.lower()
    words = lower_text.split()
    return "-".join(words)
