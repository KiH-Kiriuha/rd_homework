# task 1
x = input("Введіть число чи слово: ")
x = x.isdigit()
if x == True:
    print("Це є числом")
elif x == False:
    print("Це є словом")
