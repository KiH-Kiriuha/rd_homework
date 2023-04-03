# task 2
x = input("Введіть число чи слово: ")
def is_digit():
    return x.isdigit()

if x and is_digit():
    print("Це є число")
    x = int(x)
    if x % 2 == 0:
        print("Парне число")
    elif x % 2 == 1:
        print("Непарне число")

else:
    print("Це є слово")
