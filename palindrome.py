def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
