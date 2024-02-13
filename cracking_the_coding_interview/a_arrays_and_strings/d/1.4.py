import os
from dotenv import load_dotenv
import json


def is_palindrome_permutation(s: str) -> bool:
    letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"}
    tracker = {}
    for letter in s:
        lowerLetter = letter.lower()
        if lowerLetter in letters:
            if lowerLetter in tracker:
                del tracker[lowerLetter]
            else:
                tracker[lowerLetter] = 1
    return len(tracker) <= 1


# TEST SCRIPT
load_dotenv()

CURRENT_DIRECTORY = os.getcwd()
dir_to_book = r"\cracking_the_coding_interview"
dir_to_chapter = r"\a_arrays_and_strings"
dir_to_problem = r"\d"
file_name = r"\test.json"

dir_to_test_file = (
    rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}{file_name}"
)

f = open(dir_to_test_file)
data = json.load(f)

for input in data:
    print(f"#{input["index"]}: {is_palindrome_permutation(input["input"]["s"])== input["output"]}")
