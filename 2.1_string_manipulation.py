"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence entered by the user.
# 2. Process:The program applies four different string methods to transform the sentence.
# 3. Out:Four different versions of the original sentence.
# 4. My four transformations, and when each is useful: upper(): Useful for titles or warnings.lower(): Useful for comparing text without case differences. capitalize(): Useful for formatting the beginning of a sentence. strip(): Useful for removing unnecessary spaces.

# Your code below

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Apply four transformations
result1 = sentence.upper()
result2 = sentence.lower()
result3 = sentence.capitalize()
result4 = sentence.strip()

# Display the results
print("Uppercase:", result1)
print("Lowercase:", result2)
print("Capitalized:", result3)
print("Stripped:", result4)