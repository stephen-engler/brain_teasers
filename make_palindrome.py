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
    print(perm1)
    perm2 = len2*(len2 + 1)/2

    total_perm = perm1 + perm2

    #try 2 break each string into list of all posible substrings
    #first string
    perm_list = []
    for index in range(len1):
        len1 -= 1
        print(str1[index:])
        print(str1[:len1])
        print(str1[index:len1])
        # perm_list.append(str1[])

    #try 3 get all the 1 lenght substrings, then 2 length, then 3...up to length of string

    return total_perm

# print(make_palindrome('string', 'string'))

def make_substrings(strIn):
    substring_list = []
    str_len = len(strIn)
    for substring_size in range(str_len):
        for index_in_string in range(str_len):
            if index_in_string + substring_size < str_len:
                substring_list.append(strIn[index_in_string :index_in_string + substring_size +1 ])

    return substring_list

print(make_substrings('string'))



