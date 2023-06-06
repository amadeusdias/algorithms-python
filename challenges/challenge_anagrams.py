def quick_sort(word):
    if len(word) < 2:
        return word
    else:
        pivo = word[0]
        menores = [i for i in word[1:] if i <= pivo]
        maiores = [i for i in word[1:] if i > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)
    word1 = list(first_string.casefold())
    word2 = list(second_string.casefold())
    palavra1 = quick_sort(word1)
    palavra2 = quick_sort(word2)
    if palavra1 == palavra2:
        return (''.join(palavra1), ''.join(palavra2), True)
    return (''.join(palavra1), ''.join(palavra2), False)
