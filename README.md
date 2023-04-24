# NLP

Implementation of NLP techniques in Python. 

1. Spelling Checker:
      - Uses the technique of n-gram overlap to first find a list of candidate words that can be replaced with the word that has been spelled incorrectly. 
      - For each candidate word, the minimum edit distance is computed.
      - The word with the least edit distance is suggested as the correctly spelled word.
      
2. Fake News Detection:
      - Datset: Indian News articles. Source-https://www.kaggle.com/datasets/imbikramsaha/fake-real-news
      - contains two notebooks:
            - FakeNewsDetection.ipynb: Applies the Linear SVC classifier without any cleaning of the data
            - classifiers.ipynb: Applies more classifiers, evaluates the accuracies. Involves cleaning of the data. 
