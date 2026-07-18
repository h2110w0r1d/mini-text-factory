def clean_text(text: str) -> str:
	lower_text = text.lower()
	words = lower_text.split()
	return " ".join(words)
