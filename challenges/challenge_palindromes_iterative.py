def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    for le in range(0, int(len(word)/2)):
        if word[le] != word[len(word)-le-1]:
            return False
    return True

# font:https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
