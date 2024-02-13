# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith     ", 13
# Output: "Mr%20John%20Smith"

import os
from dotenv import load_dotenv
import json


def URLify(s, true_length):
    result = ""
    for i in range(0, true_length):
        if i > len(s) - 1:
            result += "%20"
        elif s[i] == " ":
            result += "%20"
        else:
            result += s[i]
    return result


# TEST SCRIPT
load_dotenv()

CURRENT_DIRECTORY = os.getcwd()
dir_to_book = r"\cracking_the_coding_interview"
dir_to_chapter = r"\a_arrays_and_strings"
dir_to_problem = r"\c"
file_name = r"\test.json"

dir_to_test_file = (
    rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}{file_name}"
)

f = open(dir_to_test_file)
data = json.load(f)

for input in data:
    print(f"#{input["index"]}: {URLify(input["input"]["string"], input["input"]["true_length"])== input["output"]}")

# CHATGPT Solution


def urlify(string, true_length):
    """
    Replace spaces with '%20' in a given string up to the true length.

    :param string: The input string with extra spaces at the end for padding
    :param true_length: The true length of the string excluding padding
    :return: A string with spaces replaced by '%20'
    """
    # First, trim the string to the true length to remove any extra padding at the end
    trimmed_string = string[:true_length]

    # Replace all spaces with '%20'
    urlified_string = trimmed_string.replace(" ", "%20")

    return urlified_string
