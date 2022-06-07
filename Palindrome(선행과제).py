def is_palindrome(word):
    is_true = True
    for i in range(0, int(len(word) / 2)):
        if word[i] == word[len(word)-1-i]:
            is_true = True
        else:
            is_true = False
    return is_true

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))