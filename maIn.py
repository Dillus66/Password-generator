import string
import random



# Generates a list of all letters
a = list(string.ascii_letters)

# list of all special characters
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', 
    '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', '~', '`', 
    '§', '±', '©', '®', '™', '¶', '•', 'º', 'ª', '«', '»', '¬', '¿', '¤', '€', '¢', 
    '£', '¥', '†', '‡', '◊', '∞', 'µ', '∂', '∑', '∆', '∏', '√', '∫', '≈', '≠', '≡', 
    '≤', '≥', '⊕', '⊗', '∩', '∪', '∈', '∉', '⊂', '⊃', '⊆', '⊇', '∅', '∀', '∃', '∄', 
    '∇', '⊥', '∠', '∴', '∵', '∂', '∂', '∗', '≪', '≫', '∼', '∝', '∞', '∫', '∬', '∭', 
    '∮', '∯', '∰', 'ℵ', 'ℶ', 'ℷ', 'ℸ', 'ℹ', 'ℑ', 'ℜ', 'ℵ', '⅀', '⊤', '⊥', '⊨', '⊩'
]

# Appending special characters to list a
for i in special_characters:
    a.append(i)

# Appending numbers 0 to 9 to list a
for i in range(10):
    a.append(str(i))

#Random number generator




def generate_password(password):
    # Loop 8 times
    for i in range(8):
        # Generate a random number in the range of list a
        rand_num = random.randint(0, len(a)-1)
        # concatanates random characters from list a
        password += a[rand_num]
    return password

p = ""
# call generate password. Pass P as a parameter
new_pass = generate_password(p)
print(new_pass)

