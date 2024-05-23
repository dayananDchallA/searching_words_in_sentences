# This script defines a WordSearch class that allows searching for words in a list of sentences
# using parallel processing with joblib library.

from joblib import Parallel, delayed

class WordSearch:
    def __init__(self, sentences):
        """
        Initialize the WordSearch class with a list of sentences.
        
        Parameters:
        - sentences (list): A list of strings representing sentences.
        """
        self.sentences = sentences

    def search_words_in_sentence(self, sentence, words):
        """
        Searches for words in a single sentence.
        
        Parameters:
        - sentence (str): The sentence to search within.
        - words (list): A list of words to search for.
        
        Returns:
        - list: A list of words found in the sentence.
        """
        words_in_sentence = sentence.split()
        matches = [word for word in words_in_sentence if word in words]
        return matches

    def search_words_in_sentences(self, words, n_jobs=-1):
        """
        Searches for words in the stored list of sentences using parallel processing.
        
        Parameters:
        - words (list): A list of words to search for.
        - n_jobs (int, optional): The number of parallel jobs to run. Defaults to -1 (use all available cores).
        
        Returns:
        - list: A list of words found in the sentences.
        """
        # Use parallel processing to search words in each sentence
        matches_per_sentence = Parallel(n_jobs=n_jobs)(
            delayed(self.search_words_in_sentence)(sentence, words) for sentence in self.sentences
        )

        # Flatten the list of matches
        results = [word for matches in matches_per_sentence for word in matches]

        return results

# Example usage
sentences = ["This is a sample sentence.", "Another example sentence.", "Search for words here."]
words_to_search = ["sample", "words", "search"]

word_search = WordSearch(sentences)
results = word_search.search_words_in_sentences(words_to_search, n_jobs=2)  # Configuring n_jobs
print(results)
