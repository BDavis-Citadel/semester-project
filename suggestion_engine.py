class SuggestionEngine:
    def edit_distance(self, word1, word2):
        # dynamic programming style to compute edit distance.
        rows = len(word1) + 1
        cols = len(word2) + 1
        dp = [[0] * cols for _ in range(rows)]

        # base cases
        for i in range(rows):
            dp[i][0] = i
        for j in range(cols):
            dp[0][j] = j

        # this fills in the table.
        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      
                        dp[i][j - 1],      
                        dp[i - 1][j - 1]   
                    )

        return dp[-1][-1]

    def rank_suggestions(self, word, candidates, max_suggestions=5):
        # will rank a smaller set of candidates by edit distance
        ranked = []

        for candidate in candidates:
            distance = self.edit_distance(word, candidate)
            ranked.append((distance, candidate))

        ranked.sort(key=lambda x: (x[0], x[1]))
        return [candidate for _, candidate in ranked[:max_suggestions]]

    def find_closest_words(self, word, dictionary_words, max_suggestions=5):
        # compares the input word against the full dictionary
        ranked = []

        for dictionary_word in dictionary_words:
            distance = self.edit_distance(word, dictionary_word)
            ranked.append((distance, dictionary_word))

        ranked.sort(key=lambda x: (x[0], x[1]))
        return [candidate for _, candidate in ranked[:max_suggestions]]