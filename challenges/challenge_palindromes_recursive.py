def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if low_index == len(word) or high_index < 0:
        return True

    if word[low_index] != word[high_index]:
        return False

    high_index -= 1
    low_index += 1

    return is_palindrome_recursive(word, low_index, high_index) is True
