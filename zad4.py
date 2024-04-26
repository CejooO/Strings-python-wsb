def string_made_of(string):
    if(len(string)) < 2:
        return 'Empty String'
    return string[0:2] + string[-2:]

print(string_made_of('abc'))
print(string_made_of('a'))
print(string_made_of('w3w3'))