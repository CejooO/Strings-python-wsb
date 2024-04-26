def remove_duplicates(string):
    output = []
    for i in string.split(' '):
        if i not in output:
            output.append(i)
    return output

print(remove_duplicates("Biedny Franek jest Biedny"))
