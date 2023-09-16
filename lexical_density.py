# stop_words = {"the", "and", "is", "of", "in", "to", "a", "on", "with"}

# def lexical_density(text):
#     """
#     Calculate the lexical density of a text after removing stop words.
#     Lexical density = (Number of unique words / Total number of words)
#     """
#     # Convert the text to lowercase and tokenize into words
#     words = [word for word in text.lower().split() if word not in stop_words]
    
#     # Number of unique words
#     unique_words = len(set(words))
    
#     # Total number of words
#     total_words = len(words)
    
#     # Return the lexical density
#     return unique_words / total_words if total_words != 0 else 0


import re

def tokenize(text):
    """
    Tokenizes the given text into words, removing punctuations.
    """
    # Use regular expression to tokenize the text and remove punctuations
    return re.findall(r'\b\w+\b', text.lower())

# Expanding the list of stop words
expanded_stop_words = {
    "the", "and", "is", "of", "in", "to", "a", "on", "with", "it", "for", "as",
    "are", "by", "this", "that", "an", "be", "has", "have", "from", "or", "at",
    "not", "but", "which", "if", "was", "were", "their", "they", "you", "he", 
    "she", "we", "his", "her", "our", "its"
}

def lexical_density(text):
    """
    Calculate the lexical density of a text after removing stop words.
    Lexical density = (Number of unique words / Total number of words)
    """
    # Tokenize the text
    words = [word for word in tokenize(text) if word not in expanded_stop_words]
    
    # Number of unique words
    unique_words = len(set(words))
    
    # Total number of words
    total_words = len(words)
    
    # Return the lexical density
    return unique_words / total_words if total_words != 0 else 0
