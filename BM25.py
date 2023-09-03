class BM25:
    def __init__(self, corpus, k1=1.5, b=0.75):
        self.corpus = corpus
        self.k1 = k1
        self.b = b
        self.doc_lengths = [len(doc.split()) for doc in corpus]
        self.avgdl = sum(self.doc_lengths) / len(corpus)

    def score(self, query, doc):
        """
        Compute BM25 score for a given document and query.
        """
        doc_tokens = doc.split()
        query_tokens = query.split()
        score = 0.0
        
        for token in query_tokens:
            f = doc_tokens.count(token)
            score += (f * (self.k1 + 1)) / (f + self.k1 * (1 - self.b + self.b * len(doc_tokens) / self.avgdl))
            
        return score

    def rank(self, query):
        """
        Rank documents with respect to the given query.
        """
        scores = [(i, self.score(query, doc)) for i, doc in enumerate(self.corpus)]
        return sorted(scores, key=lambda x: x[1], reverse=True)


# Example
corpus = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "Cats and dogs are animals"
]

bm25 = BM25(corpus)
query = "cat on mat"
ranking = bm25.rank(query)
print(ranking)
