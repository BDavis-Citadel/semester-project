from trie import Trie
from dictionary_loader import DictionaryLoader
from suggestion_engine import SuggestionEngine


class SpellChecker:
    def __init__(self):
        # is the main data structures used by the program.
        self.trie = Trie()
        self.loader = DictionaryLoader()
        self.suggester = SuggestionEngine()
        self.dictionary_words = []

    def load_dictionary(self, filename):
        # read all words from the dictionary file
        self.dictionary_words = self.loader.read_words(filename)

        # this inserts each word into the trie for a fast lookup.
        for word in self.dictionary_words:
            self.trie.insert(word)

    def check_word(self, word):
        # will return True if the word exists in the trie.
        return self.trie.contains(word.lower())

    def suggest_words(self, word):
        word = word.lower()

        # tries to find words that share the same first 2 letters
        prefix = word[:2] if len(word) >= 2 else word
        prefix_matches = self.trie.collect_words(prefix)

        # if prefix matches exist will rank them by edit distance.
        if prefix_matches:
            return self.suggester.rank_suggestions(word, prefix_matches)

        # if not compare it against the full dictionary.
        return self.suggester.find_closest_words(word, self.dictionary_words)

    def run(self):
        # asks the user for the dictionary file
        filename = input("Enter dictionary filename: ").strip()
        self.load_dictionary(filename)

        # this will keep checking words until the user quits
        while True:
            word = input("Enter a word to check (or type quit): ").strip().lower()

            if word == "quit":
                print("Goodbye.")
                break

            # if the word is correct it will print it.
            if self.check_word(word):
                print(f"Word is correct: {word}")
            else:
                # if the word not correct it will generate suggestions.
                print(f"Word not found: {word}")
                suggestions = self.suggest_words(word)

                if suggestions:
                    print("Did you mean:")
                    for suggestion in suggestions:
                        print(f"- {suggestion}")
                else:
                    print("No suggestions found.")