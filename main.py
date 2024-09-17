import random

print("Приветсвую, это программа для регенирации паролей")

letter = "abcdefghijklnopqrstuvwxyz"
numbers = "1234567890"
mix = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
symbols = "+-/*!&$#?=@"

vvod = input("Выберите как хотите составить пароль: 1- только из чисел, 2- только из букв, 3 - из всех символов, 4- только из символов, 5- из своих любимых символов: " )

password = ""



if vvod == "1":
    number = int(input("Напишите количество символов: "))
    for i in range(number):
        ransymbols = random.choice(numbers)
        password += ransymbols
    print(password)

if vvod == "2":
    ll = int(input("Напишите количество символов: "))
    for i in range(ll):
        ransymbols = random.choice(letter)
        password += ransymbols
    print(password)  

if vvod == "3":
    number = int(input("Напишите количество символов: "))
    for i in range(number):
        ransymbols = random.choice(mix)
        password += ransymbols
    print(password)

if vvod == "4":
    number = int(input("Напишите количество символов: "))
    for i in range(number):
        ransymbols = random.choice(symbols)
        password += ransymbols
    print(password)
    
if vvod == "5":
    number = int(input("Напишите количество символов: "))
    my_slova = input("Вводите свои символы: ")
    cc = int(input("Напиши сколько раз вам случайным образом сгенерировать пароль из ваших символов: "))           
    for _ in range(cc):  
        password = ""  
        symbols_list = list(my_slova)  
        random.shuffle(symbols_list)  
        for i in range(number):
            password += symbols_list[i % len(symbols_list)]  
        print(password)        
    pss = input("Вводите понравившийся вам пароль ")
    print("Вот пароль который вы выбрали: ", pss )    
    

if number <= 6:
    print("Слишком короткий пароль, есть возможность что вас быстро взломают ")
    
if number >= 7:
    print("Этот пароль будет трудно взломать! ")

print("Спасибо что вы пользовались нашей программой!")




    
