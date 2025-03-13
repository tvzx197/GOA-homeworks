def replace_vowels_with_exclamation(sentence):
    vowels = "aeiouAEIOU"
    return ''.join('!' if char in vowels else char for char in sentence)

# Test cases
test_sentences = [
    "Hi!", 
    "!Hi! Hi!", 
    "aeiou", 
    "ABCDE"
]

# Applying the function to the test cases
result = [replace_vowels_with_exclamation(sentence) for sentence in test_sentences]
print(result)