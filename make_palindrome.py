from is_palindrome import is_palindrome

def Make_substrings(strIn):
    """
    makes list of all possible substrings in a given string
    input: string
    output: list
    """
    substring_list = []
    str_len = len(strIn)
    #all possible lengths of a substing
    for substring_size in range(str_len):
        #each index in a string
        for index_in_string in range(str_len):
            #makes sure only full substrings(no overflow) are added to list
            if index_in_string + substring_size < str_len:
                #makes substring starting at index to the size +1(range starts at zero)
                unique_substring = strIn[index_in_string :index_in_string + substring_size +1 ]
                #appends to list
                substring_list.append(unique_substring)

    return substring_list

def Make_palindrome(str1, str2):
    """
    makes a palindrome from 2 substrings of the input
    input str1, str2 strings
    output palindrome a string OR -1 if no palindrome was found
    """
    longest_palindrome = ''

    substring_list1 = Make_substrings(str1)
    substring_list2 = Make_substrings(str2)

    for substring1 in substring_list1:
        for substring2 in substring_list2:
            possible_palindrome = substring1 + substring2
            if is_palindrome(possible_palindrome) and len(possible_palindrome) > len(longest_palindrome):
                longest_palindrome = possible_palindrome


    return longest_palindrome

print('longest palindrome ', Make_palindrome('race', 'car'))



#print(Make_substrings('string'))



