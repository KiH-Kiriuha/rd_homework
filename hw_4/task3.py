# task 3
x = input("Введіть число чи слово: ")
def is_digit():
    return x.isdigit()
def str_len(x):
    a = 0
    for i in x:
        a = a + 1
    return a

if x and is_digit():
    print("Це є число")
    x = int(x)
    if x % 2 == 0:
        print("Парне число")
    elif x % 2 == 1:
        print("Непарне число")

else:
    print("Це є слово")
    print(str_len(x))
