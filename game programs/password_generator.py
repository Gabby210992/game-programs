import random
import string

no_of_letters = int(input("How many letters do you want or your password?: \n"))
no_of_symbers = int(input("How many characters do you want in your password? :\n"))
no_of_digits = int(input("How many digit number do you want in your password? \n"))

passkey = []
for char in range(no_of_letters):
    letters = random.choice(' '.join(string.ascii_letters).split())
    passkey.append(letters)

for symbol in range(no_of_symbers):
    symbols = random.choice(' '.join(string.punctuation).split())
    passkey.append(symbols)

for num in range(no_of_digits):
    numbers = random.randint(0, 9)
    passkey.append(str(numbers))

random.shuffle(passkey)

password = ''.join(passkey)
print(f"Your password is {password}")

