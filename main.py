import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

number = int(input("Напишите количество символов:"))

password = ""

for i in range(number):
    
    ransymbols = random.choice(symbols)

    password += ransymbols
print(password)


