def fizzbuzz():
    """
    for numbers 1 to 100, if number is divisible by 3 prints fizz
    if divisible by 5 prints buzz, if by both, fizzbuzz
    if none, prints the number
    input: none
    output: none
    """
    for x in range(1,101):
        if x%3==0 and x%5==0:
            print('fizzbuzz')
        elif x%3==0:
            print('fizz')
        elif x%5==0:
            print('buzz')
        else:
            print(x)


fizzbuzz()