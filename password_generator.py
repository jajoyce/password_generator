import random
import string

length = int(input("Enter password length: "))

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
nums = string.digits
symbols = string.punctuation

characters = uppers + lowers + nums + symbols

# print(characters)
# print(type(characters))

sample = random.sample(characters, length)

# print(sample)

sample_pw = "".join(sample)

print(sample_pw)

