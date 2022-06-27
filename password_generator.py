import random
import string

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
nums = string.digits
symbols = string.punctuation
letters = uppers + lowers
characters = letters + nums + symbols

length = int(input("Enter password length: "))


if length < 1:
    print("Password length must be a positive integer.")

elif length < 8:
    first_letter = random.choice(letters)
    print(first_letter)
    sample = random.sample(characters, length - 1)
    print(sample)
    pw = first_letter + "".join(sample)
    print(pw)


