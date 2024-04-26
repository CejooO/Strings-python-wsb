def reverse_words_in_string(string):
    output = ""
    shit = string.split(' ')
    c = len(shit) - 1
    while c >= 0:
        output += shit[c] + " "
        c -= 1
    return output


print(reverse_words_in_string("Hello world"))
