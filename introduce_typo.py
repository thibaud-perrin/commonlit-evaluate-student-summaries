import random
import string

def introduce_typo(text, probability=0.05):
    """
    Introduce a typo based on a given probability.
    
    Args:
    - text (str): The input text.
    - probability (float): The probability of introducing a typo to a word.

    Returns:
    - str: Text with potential typos.
    """
    
    words = text.split()
    for i in range(len(words)):
        if random.random() < probability:
            typo_type = random.choice(["substitute", "delete", "insert", "transpose"])
            word = words[i]
            
            if typo_type == "substitute" and len(word) > 1:
                idx = random.randint(0, len(word)-1)
                char = random.choice(string.ascii_lowercase)
                word = word[:idx] + char + word[idx+1:]
                
            elif typo_type == "delete" and len(word) > 1:
                idx = random.randint(0, len(word)-1)
                word = word[:idx] + word[idx+1:]
                
            elif typo_type == "insert":
                idx = random.randint(0, len(word))
                char = random.choice(string.ascii_lowercase)
                word = word[:idx] + char + word[idx:]
                
            elif typo_type == "transpose" and len(word) > 1:
                idx = random.randint(0, len(word)-2)
                word = word[:idx] + word[idx+1] + word[idx] + word[idx+2:]

            words[i] = word

    return " ".join(words)