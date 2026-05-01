# Spell Checker Project

## Description
This project is a spell checker and word suggestion tool. It checks whether a word exists in a dictionary. If the word is not found, it suggests similar words.


## How to Run
By placing all files in the same folder and run:

```bash
python3 main.py

## Requried Input Files

#dictionary.txt

## Algorithm Implemented

# Trie to store dictionary words for fast lookup. When a user enters a word, the program first checks whether the word exists in the trie. If the word is not found, the program uses edit distance to compare the input word with dictionary words and suggest the closest matches.

## Runtime Complexity

# Trie insertion: O(L)
# Trie lookup: O(L)
# Edit distance between two words: O(mn)
