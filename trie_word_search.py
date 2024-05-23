# Trie data structure implementation for efficient word search
# and utility functions for building Trie and searching words in sentences.

class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode with an empty dictionary for children and a flag to indicate if it's the end of a word.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initializes a Trie with a root TrieNode.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Searches for a word in the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

class TrieUtils:
    @staticmethod
    def build_trie(words):
        """
        Builds a Trie data structure from a list of words.
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie

    @staticmethod
    def search_words_in_sentences(sentences, words):
        """
        Searches for words in a list of sentences using a pre-built Trie.
        """
        trie = TrieUtils.build_trie(words)
        results = []

        for sentence in sentences:
            words_in_sentence = sentence.split()  # Split the sentence into words
            for word in words_in_sentence:
                if trie.search(word):
                    results.append(word)

        return results

# Example usage
sentences = ["This is a sample sentence.", "Another example sentence.", "Search for words here."]
words_to_search = ["sample", "words", "search"]

results = TrieUtils.search_words_in_sentences(sentences, words_to_search)
print(results)
