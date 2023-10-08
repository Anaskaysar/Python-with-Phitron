def mergeStrings(word1, word2):
    merged = []
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    return ''.join(merged)

# Example usage:
word1 = "abc"
word2 = "xyz"
result = mergeStrings(word1, word2)
print(result)
