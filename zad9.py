def word_count(string):
    counter = dict();

    words = string.split()

    for i in words:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return counter

print(word_count("Witam wszystkich tu serdecznie tu"))