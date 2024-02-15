import os
from dotenv import load_dotenv
import json


def one_away(first, second):
    tracker = {}
    if abs(len(first) - len(second)) > 1:
        return False
    for letter in first:
        if letter in tracker:
            tracker[letter] += 1
        else:
            tracker[letter] = 1
    for letter in second:
        if letter in tracker:
            tracker[letter] -= 1
        else:
            tracker[letter] = 1
        if tracker[letter] == 0:
            del tracker[letter]
    if len(tracker) == 0:
        return True
    elif len(tracker) <= 2 and all(value == 1 for value in tracker.values()):
        return True
    else:
        return False


if __name__ == "__main__":
    print(one_away("asdfasdb", "asdfasdac"))

    # TEST SCRIPT
    load_dotenv()

    CURRENT_DIRECTORY = os.getcwd()
    dir_to_book = r"\cracking_the_coding_interview"
    dir_to_chapter = r"\a_arrays_and_strings"
    dir_to_problem = r"\e"
    file_name = r"\test.json"

    dir_to_test_file = (
        rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}{file_name}"
    )

    f = open(dir_to_test_file)
    data = json.load(f)

    for input in data:
        print(f"#{input["index"]}: {one_away(input["input"]["first"], input["input"]["second"])== input["output"]}")
