# My Answer

import collections


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ransom_note = collections.Counter(ransomNote)
    magazine_note = collections.Counter(magazine)
    for letter in ransom_note:
        if letter in magazine_note:
            if ransom_note[letter] > magazine_note[letter]:
                return False
        else:
            return False
    return True


# Optimal Solution
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    for i in ransomNote:
        if i in magazine:
            magazine = magazine.replace(i, "", 1)
            # third argument is count:
            # Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
        else:
            return False

    return True
