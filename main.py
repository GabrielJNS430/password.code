import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("de que longitud desea la contraseña?"))

password = ""

for i in range(longitud):
    password += random.choise(caracteres)

print(password)
