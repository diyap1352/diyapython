def word_count(str):
    counts = dict()
    words = str.split()

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts

print( word_count('Hello world have a good day.'))

