
def count_capitalized_words(text):
    """Counts words that start with a capital letter."""
    words = text.split()
    return sum(1 for word in words if word.istitle())
