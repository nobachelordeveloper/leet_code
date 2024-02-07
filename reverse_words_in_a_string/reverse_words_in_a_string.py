#My Answer
def reverseWords(self, s: str) -> str:
    list_of_words = s.split()
    reversed_list_of_words = list_of_words[::-1]
    return " ".join(reversed_list_of_words)
