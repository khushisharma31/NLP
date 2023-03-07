# NLP

Implementation of NLP techniques in Python. 

1. Spelling Checker:
      - Uses the technique of n-gram overlap to first find a list of candidate words that can be replaced with the word that has been spelled incorrectly. 
      - For each candidate word, the minimum edit distance is computed.
      - The word with the least edit distance is suggested as the correctly spelled word.
