def word_order(n, words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    unique_word_count = list(word_count.keys())
    wordcounts = list(word_count.values())

    return len(unique_word_count), wordcounts