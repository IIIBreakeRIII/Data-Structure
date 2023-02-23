# 팔린드롬

def is_palindrome(word):
    WordList = list(word)
    for i in range(len(WordList)):
        if WordList[i] == WordList[len(WordList) - 1 - i]:
            if i == len(WordList) - 1:
                return True
            else:
                continue
        else:
            return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
