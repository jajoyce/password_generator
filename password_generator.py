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
    rand_sample = random.sample(characters, length - 1)
    pw = first_letter + "".join(rand_sample)
    print(pw)

else:
    first_letter = random.choice(letters)
    rand_choices = random.choices(characters, k=length - 1)
    pw = first_letter + "".join(rand_choices)
    print(pw)
