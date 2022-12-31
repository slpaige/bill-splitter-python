def check_word(word):
    if '0' in word:
        raise NotWordError(word)
    else:
        return word


def error_handling(word):
    try:
        result = check_word(word)
        print(result)
    except NotWordError as e:
        print(e)
