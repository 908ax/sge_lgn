num = int(input("Introduce un número: "))

if num < 2:
    print(num, "no es primo")
else:
    primo = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            primo = False
        i += 1
    if primo:
        print(num, "es primo")
    else:
        print(num, "no es primo")