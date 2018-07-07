def is_palindrome(input):
    """
    If input is a palindrome, returns true
    else returns false
    input string
    output boolean
    """
    #Removes any spaces
    input = input.replace(" ", "")
    length = len(input)
    #iterates over the string
    #if first and last letters don't match returns false
    #if they do match increments the counter for first letter and decrements 
    #the counter for the last letter and checks again
    #if the counter for the first letter is greater than the last,
    #it means all letters have been checked and match 
    #returns true
    for x in range(length):
        length -= 1
        if x >= length:
            return True
        elif input[x] != input[length]:
            return False
        
# print(is_palindrome('race car'))
