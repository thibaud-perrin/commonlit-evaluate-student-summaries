stop_words = {"the", "and", "is", "of", "in", "to", "a", "on", "with"}

def lexical_density(text):
    """
    Calculate the lexical density of a text after removing stop words.
    Lexical density = (Number of unique words / Total number of words)
    """
    # Convert the text to lowercase and tokenize into words
    words = [word for word in text.lower().split() if word not in stop_words]
    
    # Number of unique words
    unique_words = len(set(words))
    
    # Total number of words
    total_words = len(words)
    
    # Return the lexical density
    return unique_words / total_words if total_words != 0 else 0

