def numberOfChars(string):
    arr = {}
    for i in string:
        chars = arr.keys()

        if i in chars:
            arr[i] += 1
        else:
            arr[i] = 1

    return arr

print(numberOfChars('uwielbiamnaukewsb'))