from random import *

lon = input("Dime la longitud de la contraseña")
chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789-.,;:;_"
password = ""

for i in range(lon):
    password = password + chars[ randint(0, len(chars)-1)]

print(password)