import string
import math

def shift_characters(word, shift):
    alphabet = string.ascii_lowercase
    char_indexes = [alphabet.index(char) for char in word]
    shifted_indexes = [(number + shift) % 26 for number in char_indexes]
    new_word = ''
    for number in shifted_indexes:
        new_word += alphabet[number]
    return new_word


print(shift_characters('abby', 5))


def pad_up_to(word, shift, n):
    new_shift = shift
    times = math.ceil(n / len(word))
    pad_string = word
    for i in range(times):
        pad_string += shift_characters(word, new_shift)
        new_shift += shift
    return pad_string[:n]


print(pad_up_to("aaa", 2, 100))


def abc_mirror(word):
    new_word = ''
    alphabet = string.ascii_lowercase
    char_indexes = [(alphabet.index(char)* -1) - 1 for char in word]
    for number in char_indexes:
        new_word += alphabet[number]
    return new_word

print(abc_mirror('az'))


def find_index(letter):
    alphabet = string.ascii_lowercase
    return alphabet.index(letter)


def create_matrix(word1, word2):
    matrix = []
    for char in word2:
        new_word = shift_characters(word1, find_index(char))            
        matrix.append(new_word)
    return matrix

print(create_matrix('mamas', 'papas'))


def get_col(matrix, n):
    col = []
    for line in matrix:
        col.append(line[n])
    return col

        

def get_cols(matrix):
    cols = []
    print(len(matrix))
    for index in range(len(matrix)-1):
        cols.append(get_col(matrix, index))
    return cols


def nested_maker(lst):
    nested_matrix = [[char for char in string] for string in lst]
    return nested_matrix


def zig_zag_concatenate(matrix):
    nested_matrix = nested_maker(matrix)
    cols = get_cols(nested_matrix)
    for col_index in range(len(cols)):
        if col_index % 2 == 1:
            cols[col_index].reverse()
    zig_zag_string = ""
    for lst in cols:
        for char in lst:
            zig_zag_string += char
    return zig_zag_string


print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


# if __name__ == '__main__':
#     name = input("Enter your name! ").lower()
#     print(f'Your key: {hash_it(name)}')
