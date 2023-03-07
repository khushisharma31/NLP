with open('input.txt', 'r') as f:
    word = f.read().strip()

with open('big.txt', 'r') as f:
    dictionary = [line.strip() for line in f.readlines()]

def ngram_overlap(s1, s2, n):
    s1_ngrams = set([s1[i:i+n] for i in range(len(s1)-n+1)])
    s2_ngrams = set([s2[i:i+n] for i in range(len(s2)-n+1)])
    return len(s1_ngrams.intersection(s2_ngrams))

# Define a function to compute the minimum edit distance between two strings
def min_edit_distance(source, target):
    n = len(source)
    m = len(target)
    D = [[0] * (m+1) for i in range(n+1)]
    for i in range(n+1):
        D[i][0] = i
    for j in range(m+1):
        D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if source[i-1] == target[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1
    return D[n][m]

# Define a function to suggest words from the dictionary based on n-gram overlap
def suggest_words(word, n, num_suggestions=10):
    word = word.lower()
    scores = [(w, ngram_overlap(word, w.lower(), n)) for w in dictionary if w.lower() != word and len(w) >= n]
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    suggestions = [s[0] for s in scores[:num_suggestions]]
    return suggestions

# Get a list of suggested words based on n-gram overlap
suggestions = suggest_words(word, 2)


distances = [(w, min_edit_distance(word, w)) for w in suggestions]
print(distances)

closest_word = min(distances, key=lambda x: x[1])[0]

# Output the closest word to the console
print(f"Input word: {word}")
print(f"Suggested word: {closest_word}")

