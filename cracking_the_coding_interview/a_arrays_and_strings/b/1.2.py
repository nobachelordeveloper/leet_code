# Given two strings, write a method to decide if one is a permutation of the other.
import os
from dotenv import load_dotenv
import json


def isPermutation(str1, str2):
    letterCount1 = {}
    letterCount2 = {}
    for letter in str1:
        if letter in letterCount1:
            letterCount1[letter] += 1
        else:
            letterCount1[letter] = 1
    for letter in str2:
        if letter in letterCount2:
            letterCount2[letter] += 1
        else:
            letterCount2[letter] = 1
    return letterCount1 == letterCount2


# TEST SCRIPT
load_dotenv()

CURRENT_DIRECTORY = os.getcwd()
dir_to_book = r"\cracking_the_coding_interview"
dir_to_chapter = r"\a_arrays_and_strings"
dir_to_problem = r"\b"
file_name = r"\test.json"

dir_to_test_file = (
    rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}{file_name}"
)

f = open(dir_to_test_file)
data = json.load(f)

for input in data:
    print(isPermutation(input["string1"], input["string2"]) == input["output"])
