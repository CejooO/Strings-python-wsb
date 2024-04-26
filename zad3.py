def odd_index(string):
    final_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            final_string = final_string + string[i]
    return(final_string)

print(odd_index("Sprawdzamcodrugiznak"))

