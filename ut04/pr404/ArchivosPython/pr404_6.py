prod1 = {
    "Pan": 1.5,
    "Leche": 2.0,
    "Huevos": 3.5
}

prod2 = {
    "Leche": 1.8,
    "Arroz": 2.5,
    "Huevos": 3.0
}

def combDic(dic1, dic2):
    combinado = dic1.copy()
    for producto, precio in dic2.items():
        if producto in combinado:
            combinado[producto] += precio
        else:
            combinado[producto] = precio
    return combinado

comb = combDic(prod1, prod2)
print(comb)