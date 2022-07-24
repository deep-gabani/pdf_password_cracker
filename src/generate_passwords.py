"""Generates all possible combinations of passwords for the given arguments."""
from itertools import product
import typing as t

ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '39315'
SPECIAL_CHARS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
WHITESPACE = ' \t\n\r\x0b\x0c'


def generate_passwords(password_length: int,
                       letters: bool,
                       digits: bool,
                       special_chars: bool,
                       whitespace: bool) -> t.List[str]:
    """
    Create a list of potential passwords for the given total number of letters.

    Args:
        password_length: The total number of letters in the password.
        digits: Flag to indicate if there are digits in the password.
        special_chars: Flag to indicate if there are special characters in the
                       password.
        whitespace: Flag to indicate if there are whitespace in the password.
    Returns:
        A list of potential passwords.
    """
    possible_chars = ''
    if letters:
        possible_chars += ASCII_LETTERS
    if digits:
        possible_chars += DIGITS
    if special_chars:
        possible_chars += SPECIAL_CHARS
    if whitespace:
        possible_chars += WHITESPACE

    # Convert the letters into a list of characters.
    possible_chars_list = list(possible_chars)

    # Compute all possible combinations of length: password_length.
    all_combinations = product(possible_chars_list, repeat=password_length)
    all_combinations = [''.join(c) for c in all_combinations]

    print(f'Found {len(all_combinations)} possible combinations...')
    return all_combinations
