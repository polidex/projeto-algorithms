def sort_string(string):
    if len(string) <= 1:
        return string

    firstLetter = string[0]
    first_index = [letter for letter in string[1:] if letter < firstLetter]
    last_index = [letter for letter in string[1:] if letter >= firstLetter]

    return sort_string(first_index) + [firstLetter] + sort_string(last_index)


def is_anagram(first_string, second_string):
    if (first_string == '') and (second_string == ''):
        return ('', '', False)

    first_word = first_string .lower()
    second_word = second_string.lower()

    return (''.join(sort_string(list(first_word))),
            ''.join(sort_string(list(second_word))),
            ''.join(sort_string(list(first_word)))
            == ''.join(sort_string(list(second_word))))