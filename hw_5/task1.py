# task 1
text = input("Введіть: ")

for char in text:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f"Це {char} - парне число.")
        else:
            print(f"Це {char} - непарне число.")
    elif char.isalpha():
        if char.isupper():
            print(f"Це {char} - велика літера.")
        else:
            print(f"Це {char} - маленька літера.")
    else:
        print("Це ", char)
