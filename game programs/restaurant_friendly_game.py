import random

names = input("Please enter your names separated by a comma: \n").upper()
modified_names = names.split(",")
# random_name = random.randint(0, (len(modified_names)-1))

payer = random.choice(modified_names)
print(f"{payer} is selected. YOu have to pay the bills!")