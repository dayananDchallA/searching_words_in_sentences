import mmap

class WordSearch:
    """
    A class to perform word search in sentences using memory-mapped files.
    """

    def __init__(self, filename):
        """
        Initialize the WordSearch class with a filename of a text file containing sentences.
        
        Parameters:
        - filename (str): The path to the text file containing sentences.
        """
        self.filename = filename

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

    def search_words_in_sentences(self, words):
        """
        Searches for words in the sentences stored in the text file using memory-mapped files.
        
        Parameters:
        - words (list): A list of words to search for.
        
        Returns:
        - list: A list of words found in the sentences.
        """
        results = []

        with open(self.filename, "r", encoding="utf-8") as file:
            with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                mm.seek(0)
                data = mm.readline()
                while data:
                    sentence = data.decode("utf-8").strip()
                    matches = self.search_words_in_sentence(sentence, words)
                    results.extend(matches)
                    data = mm.readline()

        return results

# Example usage
filename = "sentences.txt"  # Assuming sentences are stored in a file named "sentences.txt"
words_to_search = ["sample", "words", "search"]

word_search = WordSearch(filename)
results = word_search.search_words_in_sentences(words_to_search)
print(results)
