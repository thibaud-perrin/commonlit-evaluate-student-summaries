import re


stop_words = {"the", "and", "is", "of", "in", "to", "a", "on", "with"}

def remove_stop_words(text):
    """
    Remove stop words from the text.
    """
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def readability_scores(text):
    text = remove_stop_words(text)  # Remove stop words from the text
    
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if len(s) > 0]
    
    total_sentences = len(sentences)
    total_words = sum(len(s.split()) for s in sentences)
    total_syllables = sum(count_syllables(word) for word in re.findall(r'\w+', text))
    polysyllable_count = sum(1 for word in re.findall(r'\w+', text) if count_syllables(word) >= 3)
    
    # Flesch-Kincaid Grade Level
    FK_grade = 0.39 * (total_words/total_sentences) + 11.8 * (total_syllables/total_words) - 15.59
    
    # Gunning Fog Index
    Gunning_Fog = 0.4 * ((total_words/total_sentences) + 100 * (polysyllable_count/total_words))
    
    # SMOG Index
    SMOG = 1.043 * (30 * polysyllable_count/total_sentences)**0.5 + 3.1291
    
    return FK_grade, Gunning_Fog, SMOG


