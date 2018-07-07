#find longest word in sentence

def find_longest_word(sentence):
    longest_word = ""
    words = sentence.split()
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word

    return longest_word

print(find_longest_word('i am a '))