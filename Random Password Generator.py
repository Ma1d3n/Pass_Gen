import random
import string

print("Hello, let's generate your password!")
l = int(input("Enter the length of the password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, l)
password = "".join(temp)
print(password)

