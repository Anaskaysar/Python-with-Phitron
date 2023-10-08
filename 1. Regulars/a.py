def mergeStrings(word1, word2):
    merged = []
    min_len = min(len(word1), len(word2))

    for i in range(min_len):
        merged.append(word1[i])
        merged.append(word2[i])

    # If one word is longer than the other, add the remaining characters
    merged.extend(word1[min_len:])
    merged.extend(word2[min_len:])

    return ''.join(merged)

