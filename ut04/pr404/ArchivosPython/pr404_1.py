frutas = {
    "manzana": ["1.25"],
    "limon": ["2.00"],
    "fresa": ["0.50"],
    "platano": ["1.75"],
}

fruta = input("Ingresa el nombre de una fruta: ").lower()

if fruta in frutas:
    print("El precio de la", fruta, "es de", frutas[fruta], "€")
else:
    print("Lo sentimos, la fruta", fruta, "no está disponible.")
