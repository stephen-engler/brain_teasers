def is_palindrome(input):
    input = input.replace(" ", "")
    length = len(input)
    for x in range(length):
        if input[x] != input[length -1]:
            return False
        length -= 1
    return True


print(is_palindrome('race car'))