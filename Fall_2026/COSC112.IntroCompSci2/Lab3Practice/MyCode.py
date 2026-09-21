def character_counter(sentence):
    vowels = 0 
    consonants = 0
    characters = 0

    for char in sentence:
        if char.isalpha():
            characters += 1

            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
    print ( "Total characters (excluding spaces):", characters)
    print("Vowel count:", vowels)
    print("Consonant count:", consonants)

    
# Test your task1 with three test cases
sentence=input("Enter a sentence: ")
character_counter(sentence)

# Task2(15pts) - Reversing Words in a Sentence

def reverse_words(sentence):
    #reverse the order of words in a given sentence.
    #Returns The reversed sentence.
    words = sentence.split()
    reversed_sentence = " "

    for word in words:
        reversed_sentence = word + " " + reversed_sentence

    return reversed_sentence.strip()
    
# Test your task2 with 3 test cases
sentence=input("Enter a sentence: ")
print("Reversed sentence:",reverse_words(sentence))

# Task3(20pts) - Palindrome Checker
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


# Test your task3 with three test cases
word=input("Enter a word: ")
#print results if the word is palindrome or not
if is_palindrome(word):
    print ("It is a palindrome!")
else:
    print ("It is not a palindrome!")
