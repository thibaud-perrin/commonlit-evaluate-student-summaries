import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def calc_tf_idf(question, text, N = 5):
    # Concatenate question and text
    combined_text = question + " " + text
    
    # Initialize a TF-IDF vectorizer with 1-grams, 2-grams, and 3-grams
    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 1), stop_words='english')
    
    # Compute the TF-IDF scores for terms in the text
    tfidf_scores = tfidf_vectorizer.fit_transform([combined_text])
    
    # Extract the non-zero elements and sort them in descending order to get top terms
    non_zero_elements = tfidf_scores.nonzero()[1]
    terms_scores = [(tfidf_vectorizer.get_feature_names_out()[index], tfidf_scores[0, index]) for index in non_zero_elements]
    sorted_terms = sorted(terms_scores, key=lambda x: x[1], reverse=True)[:N]
        
    return [term[0] for term in sorted_terms]

# def calc_tf_idf(data):
#     df = pd.DataFrame(data)
    
#     # Flattening the data
#     rows = []
#     for _, row in df.iterrows():
#         for answer in row['answers']:
#             rows.append((row['question'], row['text'], answer))
#     flat_df = pd.DataFrame(rows, columns=['question', 'text', 'answer'])
    
#     # Combine 'question', 'text', and 'answer' for TF-IDF vectorization
#     flat_df['combined_text'] = flat_df['question'] + ' ' + flat_df['text'] + ' ' + flat_df['answer']
    
#     # TF-IDF vectorization
#     tfidf_vectorizer = TfidfVectorizer(max_df=0.85, max_features=10000, stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(flat_df['combined_text'])
#     tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    
#     # Storing tuple of word and score for each question in a new DataFrame
#     word_score_data = {'question': [], 'word_score_tuples': []}
#     for index, row in flat_df.iterrows():
#         word_score_data['question'].append(row['question'])
#         word_score_data['word_score_tuples'].append([(word, score) for word, score in zip(tfidf_vectorizer.get_feature_names_out(), tfidf_df.iloc[index]) if score > 0])
    
#     word_score_df = pd.DataFrame(word_score_data)
    
#     return word_score_df