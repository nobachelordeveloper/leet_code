import os
from dotenv import load_dotenv
import json
from _1_5 import one_away
from solution import solution

# TEST SCRIPT
load_dotenv()

CURRENT_DIRECTORY = os.getcwd()
dir_to_book = r"\cracking_the_coding_interview"
dir_to_chapter = r"\a_arrays_and_strings"
dir_to_problem = r"\e"
file_name = r"\test_data.json"
# file_name = r"\test_data2.json"
dir_to_test_file = (
    rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}{file_name}"
)
test_results_FileName=rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}\test_results.json"
test_FileName=rf"{CURRENT_DIRECTORY}{dir_to_book}{dir_to_chapter}{dir_to_problem}\test.json"

f = open(dir_to_test_file)
data = json.load(f)
f.close()

errors = []
test = []
index = 1
for inputLine in data:
    input = inputLine["input"]
    left_side = one_away(input["first"], input["second"])
    right_side = solution(input["first"], input["second"])
    isMatch = left_side == right_side
    test.append(
        {"index": index, "input": input, "output": right_side}
    )
    if not isMatch:
        errors.append(
            {"index": index, "my_ans": left_side, "given": right_side, "input":input}
        )
    index += 1
if len(errors) > 0:
    for error in errors:
        print(f"There was an error at index #{error["index"]}")
        print(f"My answer was: {error["my_ans"]}")
        print(f"Given ans was: {error["given"]}")
    json_object = json.dumps(errors, indent=4)
    f = open(test_results_FileName, "w")
    f.write(json_object)
    f.close()
else:
    print("All the outputs matched!")
    json_object = json.dumps(test, indent=4)
    f = open(test_FileName, "w")
    f.write(json_object)
    f.close()
    if(os.path.isfile(test_results_FileName)):
        os.remove(test_results_FileName)
