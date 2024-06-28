def my_list(items):
    spam.insert(-1, "and")
    for item in range (len(spam)):
        print(spam[item], end= ", " if item < len(spam) - 2 else " ")
    print()
    
spam = ['apples', 'bananas', 'tofu', 'cats']
print(my_list(spam))