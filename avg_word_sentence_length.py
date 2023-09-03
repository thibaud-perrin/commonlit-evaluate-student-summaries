stop_words = {"the", "and", "is", "of", "in", "to", "a", "on", "with"}

def remove_stop_words(text):
    """
    Remove stop words from the text.
    """
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def average_word_length(text):
    """
    Compute the average length of words in the text.
    """
    words = remove_stop_words(text).split()
    total_word_length = sum(len(word) for word in words)
    return total_word_length / len(words) if words else 0

def average_sentence_length(text):
    """
    Compute the average length of sentences in the text.
    """
    # Splitting sentences on '.', '!', and '?' might be simplistic and may not handle all cases.
    # For a more robust solution, regular expressions or NLP libraries would be recommended.
    sentences = [s.strip() for s in text.split('.') if s]
    total_sentence_length = sum(len(remove_stop_words(sentence).split()) for sentence in sentences)
    return total_sentence_length / len(sentences) if sentences else 0