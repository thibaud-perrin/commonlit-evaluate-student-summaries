import re

def potential_splits(text, MIN_LENGTH = 20):
    for match in re.finditer(r', (and|each|according|the|but|or)', text):
        start_idx = match.start()
        
        # Check the length of the potential sentence
        potential_sentence = text[:start_idx]
        if len(potential_sentence.split()) >= MIN_LENGTH:
            yield start_idx, match.group(1)


def Second_split(text, MIN_LENGTH=20):
    # Identify positions where we might insert periods
    break_points = [
        "however", "therefore", "moreover", "furthermore", 
        "because", "and", "if", "but", "yet", "although",
        "though", "meanwhile", "while", "when", "since",
        "unless", "as", "so", "or"
    ]

    re_txt = r'('
    for i, bp in enumerate(break_points):
        if i > 0:
            re_txt += '|'
        re_txt +=  '\s{1}' + bp + '\s{1}'
    re_txt += r')'

    def pt_split(text, MIN_LENGTH = 20):
        # Find all occurrences of the breakpoint
        bp = 'but'
        for match in re.finditer(re_txt, text):
            start_idx = match.start()
            # Split the text at the breakpoint
            potential_sentence = text[:start_idx]
            if len(potential_sentence.split()) >= MIN_LENGTH:
                yield start_idx, match.group(1)[1:]
    
    for start_idx, conjunction in pt_split(text, MIN_LENGTH):
        text = text[:start_idx] + '. ' + conjunction.capitalize() + text[start_idx + 2 + len(conjunction) - 1:]
    # Post-process the text to fix any capitalization issues at the start
    return text

def Add_Periods(text, MIN_LENGTH = 20):
    for start_idx, conjunction in potential_splits(text, MIN_LENGTH):
        text = text[:start_idx] + '. ' + conjunction.capitalize() + text[start_idx + 2 + len(conjunction):]
    
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    if len(sentences) == 1 and len(text.split(' ')) > MIN_LENGTH * 1.5:
        text = Second_split(text, 10)
    return text