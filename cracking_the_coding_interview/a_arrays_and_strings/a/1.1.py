# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

string_one = "hello"
string_two = "world"
string_three = "apple"
string_four = "12345"
string_five = "abracadabra"

def isUniqueCharacters(str):
    # Creating a hash table using a dictionary
    hash_table = {}

    for letter in str:
        if not letter in hash_table:
            hash_table[letter] = 1
        else:
            return False
    return True


print(isUniqueCharacters(string_one))
print(isUniqueCharacters(string_two))
print(isUniqueCharacters(string_three))
print(isUniqueCharacters(string_four))
print(isUniqueCharacters(string_five))
