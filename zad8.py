def longest_word_in_list(string):
    string_lens = []
    for i in string:
        string_lens.append((len(i), i))

    string_lens.sort()
    return string_lens[-1][0], string_lens[-1][1]

result = longest_word_in_list(["SKUN", "TIBIA.PL", "MALYSZ DOBRZE SKAKAL"])
print("Longest word ", result[1])
print("Length of longest word ", result[0])

