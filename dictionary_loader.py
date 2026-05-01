class DictionaryLoader:
    def read_words(self, filename):
        # it reads words from a file. It reads one word per line.
        words = []
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    words.append(word)
        return words
    