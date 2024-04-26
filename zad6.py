def reverse_string_by_four(string):
    if len(string) % 4 == 0:
        return ''.join(reversed(string))

    return string

print(reverse_string_by_four("Helloswiecieheh"))
print(reverse_string_by_four("Siemacotamuc"))