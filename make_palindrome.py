from is_palindrome import is_palindrome

def make_palindrome(str1, str2):
    """
    makes a palindrome from 2 substrings of the input
    input str1, str2 strings
    output palindrome a string OR -1 if no palindrome was found
    """
    # find total amout of permutiations
    len1 = len(str1)
    len2 = len(str2)

    perm1 = len1*(len1+1)/2
    perm2 = len2*(len2 + 1)/2

    total_perm = perm1 + perm2

    return total_perm

print(make_palindrome('string', 'string'))